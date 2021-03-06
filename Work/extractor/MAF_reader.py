# MAF_reader
# Created by JKChang
# 2019-02-11, 20:43
# Tag:
# Description: read MAF file

import re

import numpy as np
import pandas as pd
import paramiko

import config
from Work.extractor.studyList import getStudyIDs


class MAFstatus():
    def __init__(self, studyID, fullsize, annotated, unknown):
        self.studyID = studyID
        self.fullsize = fullsize
        self.annotated = annotated
        self.unknown = unknown


def investigation_reader(studyID, prefix):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(config.SSH_PARAMS['host'], username=config.SSH_PARAMS['user'],
                   password=config.SSH_PARAMS['password'])
    sftp_client = client.open_sftp()
    address = '/net/isilonP/public/rw/homes/tc_cm01/metabolights/prod/studies/stage/private/' + studyID + '/i_Investigation.txt'
    try:
        with sftp_client.open(address) as f:
            for line in f.readlines():
                if line.startswith(prefix + '\t'):
                    fileNames = list(re.findall(r'"([^"]*)"', line))
                    return fileNames
    except:
        print('Fail to read investigation file from ' + studyID)


def assay_reader(filePath, colName):
    try:
        df = pd.read_csv(filePath, sep='\t')
        return list(df[colName].dropna().unique())
    except:
        print('Fail to read assay file from ' + filePath)


FolderPath = r'/Volumes/GoogleDrive/My Drive/study_metadata_backup/'
studyIDs = getStudyIDs(publicStudy=True)
res = []
count = 0
unknown_terms = []

for studyID in studyIDs:
    count += 1
    print(studyID)
    studyPath = FolderPath + studyID + '/'
    study_full, study_annotated, study_unknown = 0, 0, 0

    try:
        assayList = investigation_reader(studyID, 'Study Assay File Name')
        mafList = []

        for assay in assayList:
            mafList += assay_reader(studyPath + assay, 'Metabolite Assignment File')
            mafList = list(set(mafList))

        try:
            if len(mafList) > 0:
                for maf_file in mafList:
                    try:
                        df = pd.read_csv(studyPath + maf_file, sep='\t')
                        # df = df.astype(str)
                        annotated = df.loc[
                            (df['database_identifier'].notnull()) | (df['metabolite_identification'].notnull())]
                        unknown = annotated.loc[~annotated['database_identifier'].astype(str).str.startswith(
                            ('CHEBI', 'HMDB', 'CSID', 'TG', 'DG', 'P', 'L', 'C', 'SM', 'PubChem'), na=True)]

                        term = list(unknown['database_identifier'].unique())
                        unknown_terms = unknown_terms + list(set(term) - set(unknown_terms))
                        study_full += df.shape[0]
                        study_annotated += (annotated.shape[0] - unknown.shape[0])
                        study_unknown += unknown.shape[0]

                    except:
                        print(studyID, maf_file)
                        continue
        except:
            print('Fail to load MAF file from ', studyID)
            continue

        status = MAFstatus(studyID, fullsize=study_full, annotated=study_annotated, unknown=study_unknown)
        res.append(status)
    except:
        print('Fail to load investigation file from ', studyID)
        continue

# print(unknown_terms)
# cols = ['database_identifier','metabolite_identification']

df = pd.DataFrame(columns=['studyID', 'annotated', 'unknown', 'un-annotated'])
for maf in res:
    # try:
    unannotated = maf.fullsize - maf.annotated - maf.unknown
    # print(unannotated)
    temp = pd.Series([maf.studyID, maf.annotated, maf.unknown, unannotated],
                     index=df.columns)
    df = df.append(temp, ignore_index=True)
    # except:
    #     print('something wrong with' + maf.studyID)
df.replace(0, np.nan)

df.to_csv('maf_results.tsv', sep='\t', index=False)
