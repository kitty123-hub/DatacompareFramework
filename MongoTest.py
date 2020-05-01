from random import randint
import datacompy
import pymongo
import pandas as pd

#import sys
#sys.path.append('C:/Users/srikrishna.r/PycharmProjects/Learnings/src/Connections/')

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient.TestDatabase

#mydb.validate_collection(name_or_collection='reviews')
#print(mydb.list_collection_names())

mydb.reviews.delete_many({})


names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
company_type = ['LLC','Inc','Company','Corporation']
company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
for x in range(1, 501):
    business = {
        "id": mydb.reviews.find().count()+1,
        'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
        'rating' : randint(1, 5),
        'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))]
    }
    #Step 3: Insert business object directly into MongoDB via isnert_one
    result=mydb.reviews.insert_one(business)
    #Step 4: Print to the console the ObjectID of the new document
        #print('Created {0} of 100 as {1}'.format(x,result.inserted_id))
    #Step 5: Tell us that you are done
        #print('finished creating 100 business reviews')

#Read data from MongoDB and make a data frame
Documents = mydb.reviews.find({},{'_id':0})
df = pd.DataFrame.from_records(list(Documents))
#print (df)


#Read Excel and make a data frame
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






