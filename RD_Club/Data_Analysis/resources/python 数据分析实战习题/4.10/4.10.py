import pandas
from pandas import read_csv

data1 = read_csv(
    'D:\\PDA\\4.10\\data1.csv', sep="|"
)
data2 = read_csv(
    'D:\\PDA\\4.10\\data2.csv', sep="|"
)
data3 = read_csv(
    'D:\\PDA\\4.10\\data3.csv', sep="|"
)
data = pandas.concat([data1, data2, data3])

data = pandas.concat([
    data1[[0, 1]], 
    data2[[1, 2]], 
    data3[[0, 2]]
])
