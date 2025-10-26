import pandas as pd


# a=pd.Series([1,2,3])

# print(a,type(a))


# series with index
b=pd.Series(["yatender", "golu", 'mayank'],index=[1,2,3])

print(b)
print(b[0:2])

dictionary=pd.Series({1:"golu",
                      2:"mayank",
                      3:"anand"})

print(dictionary)
print(dictionary[1:3])



