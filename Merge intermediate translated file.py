import pandas as pd
import os
#checking all translated files
arr = os.listdir("intermediate\\")
#creating blank data frame
df=pd.DataFrame()
#iterate through translated file and merge them
for i in arr:
    df2=pd.read_excel("intermediate\\"+i)
    df=df.append(df2)
df=df.replace('"', '', regex=True)

print("Shape of translated Data Frame :: "+str(df.shape))

df = df.iloc[:, 2:]
df.to_excel("merged_file.xlsx")