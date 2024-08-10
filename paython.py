import pandas as pand

df = pand.read_csv('Employees.csv')
print(df)

df.drop_duplicates(inplace=True)
# print(df)

df['Age'] = df['Age'].astype(int)
# print(df)

df['Salary in EGP'] = df['Salary(USD)']*50
# print(df)

print('The Average Age is:', df['Age'].mean())
# print(df)

print('The Median Salary is:', df['Salary in EGP'].median())
# print(df)

print('The Ratio Between Male and Female is:', df['Gender'].value_counts()['M'] / df['Gender'].value_counts()['F'])
# print(df)

df.to_csv('Employees_Updated.csv', index=False)
print(df)

