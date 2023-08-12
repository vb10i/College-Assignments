import pandas as pd
dictionary=[{'a':10}, {'b':20}, {'c':30}]
example=pd.DataFrame(dictionary)
#print(example)

result={'Vansh':pd.Series([20,18,19],index=['python','calculus','electronics']), 'Arya':pd.Series([16,19,19],index=['python','calculus','electronics']), 'Ashok':pd.Series([18,18,18],index=['python','calculus','electronics'])}
result_output=pd.DataFrame(result)
print("mid term result 2023:")
print(result_output)

s1=[20,18,19]
s2=[16,19,19]
s3=[18,18,18]
s1.index=['python','calculus','electronics']
s2.index=['python','calculus','electronics']
s3.index=['python','calculus','electronics']
print(s1)


