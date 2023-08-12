import pandas as pd
s1=[1,2,3,4]
index=[10,20,30,40]
series=pd.Series(s1,index)
#print(series)

series2=pd.Series([5,6,7,8],index=[50,60,70,80])
#print(series2)

series3=pd.Series([18,17,19],index=['maths','chemistry','physics'])
#print(series3)

dict1={"India":"Delhi", "UK":"London", "USA":"New York"}
series=pd.Series(dict1)
#print(series)

dict2={"Messi":1, "Mbappe":2, "Haland":3, "KDB":4, "Vinicius":5}
series=pd.Series(dict2)
#print("Ballon d'or rankings 2023:")
#print(series)


series4=pd.Series(["Messi","Mbappe","Haland","KDB","Vinicius"],index=[1,2,3,4,5])
print("bdor rankings 2023:")
print(series4)
print(series4[2])
print(series4[2:4])
series4.index=['I','II','III','IV','V']
print(series4)
print( )
print("bdor list in reverse order:")
print(series4[::-1])




