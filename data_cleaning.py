import pandas as pd
import datetime
print("Start time :: "+str(datetime.datetime.now()))
from googletrans import Translator

#reading raw data and removing course_id as it won't be helpful hence took only 2 cols
df=pd.read_csv("ML - Topic Prediction\\course_metadata.csv",usecols=['title', 'description'])
#fillna
df=df.fillna('NaN')
#removing duplicates in data frame
df.drop_duplicates(inplace=True)
#replace special chars
df=df.replace(r'<[^<>]*>', '', regex=True)
df=df.replace(to_replace=["??","..","||"],value="")
#translating data frame languages to english
#splitting data frame for translation as it takes heavy load on api as api works on internet so
#batching and creating files with 2K records
i=0;
while (i < df.shape[0]):
    df2=df.iloc[i:i+2000,:]
    translator = Translator()
    i = i + 2000
    print("iteration " + str(i / 2000) + " started")
    df2['title_en'] =df2['title'].apply(translator.translate,  dest='en').apply(getattr, args=('text',))
    df2['description_en'] = df2['description'].apply(translator.translate,  dest='en').apply(getattr, args=('text',))
    df2 = df2.applymap(lambda s: s.lower() if type(s) == str else s)
    df2.to_excel("intermediate\\"+str(i/2000)+".xlsx")
    print("iteration "+str(i/2000)+ " completed")


print("End time :: "+str(datetime.datetime.now()))