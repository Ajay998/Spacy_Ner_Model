# import mysql.connector
# db=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     autocommit = True,
#     database="demomrat_mrattestai_staging"
# )
# mycursor = db.cursor()

import json

def save_data(file,data):
  with open(file,"w",encoding="utf-8") as f:
    json.dump(data,f,indent=4)

import pandas as pd
list=[]
data= pd.read_csv("hello1.csv")
x_= data.iloc[:,:6].values
for x in x_:
   print(x[0])
   list.append(x[0])

save_data("titles1.json", list)
