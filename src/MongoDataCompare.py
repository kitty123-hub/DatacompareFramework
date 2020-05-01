import urllib
from random import randint
import datacompy
from src.Connections import MongoDBConnector
import pandas as pd


conn = MongoDBConnector.DbConnect('','127.0.0.1', 27017,'')
mydb = conn.TestDatabase
print(mydb.list_collection_names())
#mydb.reviews.delete_many({})


#Read data from MongoDB and make a data frame
Documents = mydb.reviews.find({},{'_id':0})
df = pd.DataFrame.from_records(list(Documents))


# ExcelData = pd.read_excel(open(r'C:\Users\srikrishna.r\PycharmProjects\Learnings\test.xlsx', 'rb'),sheet_name='sheet1')
ExcelData = pd.read_excel(r'C:\Users\srikrishna.r\PycharmProjects\Learnings\test.xlsx')
df1 = pd.DataFrame(ExcelData)
#print (df1)


compare = datacompy.Compare(
    df, df1,
    join_columns='id',  # You can also specify a list of columns eg ['policyID','statecode']
    abs_tol=0,  # Optional, defaults to 0
    rel_tol=0,  # Optional, defaults to 0
    df1_name='Original',  # Optional, defaults to 'df1'
    df2_name='New'  # Optional, defaults to 'df2'
)

print (compare.report())



