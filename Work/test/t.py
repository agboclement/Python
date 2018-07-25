# t
# Created by JKChang
# 26/06/2018, 14:47
# Tag:
# Description: 

from owlready2 import *

from Work.ontology_info import *

# onto = get_ontology('file:///Users/jkchang/Downloads/abbc.owl').load()

onto = get_ontology('./abbc.owl').load()
with onto:
    class Drug(Thing):
        pass


    class HealthProblem(Thing):
        pass


    class is_prescribed_for(Drug >> HealthProblem):
        pass
    class pharmaceutical_comment(comment):
        pass

    class my_annotation(AnnotationProperty):
        pass


    class pharmaceutical_comment(comment):
        pass



    acetaminophen = Drug("acetaminophen")
    pain = HealthProblem("pain")

    acetaminophen.is_prescribed_for.append(pain)
    comment[acetaminophen, is_prescribed_for, pain] = "A comment on the acetaminophen˓→pain relation"




    onto.save(file="abbc.owl", format="rdfxml")



# apple.comment = ["A first comment on the Drug class", "A second comment"]
# onto.save(file="abbc.owl", format="rdfxml")

# res = onto.search_one(label ='apple')
# res.__getattribute__()



# f = information(onto)
# print(f.get_supers('pink lady'))
# print(f.super_count('pink lady'))
# print(f.get_subs('Investigator'))
# print(f.sub_count('http://purl.enanomapper.org/onto/ENM_9000014'))
# print(f.get_iri('pink lady'))
