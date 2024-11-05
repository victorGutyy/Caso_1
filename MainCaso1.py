import pandas as pd

path = '2017_2019.csv'
var_solares = pd.read_csv(path, encoding='latin1')
print(type(var_solares))
print(var_solares)
