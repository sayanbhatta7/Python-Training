# install the mongodb on local
# checked cli by using mongo --host

# 1. Database up and running
# python,  + mongo ===> pymongo

# 1. connect to mongodb using python

import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def main():
    try:
        myclient = MongoClient("mongodb://%s:%s@127.0.0.1" %('sayan', 'minion123'))
       # print("coed...", mydb)
        #database
        db=myclient.database
        # Created or Switched to collection names: my_gfg_collection
        collection = db.my_gfg_collection

        emp_rec1 = {
            "name": "Mr.Geek",
            "eid": 24,
            "location": "delhi"
        }
        emp_rec2 = {
            "name": "Mr.Shaurya",
            "eid": 14,
            "location": "delhi"
        }

        # Insert Data
        rec_id1 = collection.insert_one(emp_rec1)
        rec_id2 = collection.insert_one(emp_rec2)

        print("Data inserted with record ids", rec_id1, " ", rec_id2)

        # Printing the data inserted
        cursor = collection.find()
        for record in cursor:
            print(record)





    except ConnectionFailure as e:
        print("error", e)

if __name__ == '__main__':
    main()



#  #create collection
        # collection = db.mydb['student']
        # record = {
        #     "_id":0,
        #     "name": "raj",
        #     "roll_number": 101,
        #     "branch": "cse",
        #     "marks": 40
        #
        # }
        # record_1 = collection.insert_one(record)
        # print("records", record_1)
        #
        #  # list down the databases
        # list_of_db = myclient.list_database_names()
        # print("databases available in mongodb after creation", list_of_db)
        #
        # records = {
        #     "record1":{
        #                     "_id": 17,
        #                     "name": "rohan",
        #                     "roll_number": 103,
        #                     "branch": "cse",
        #                     "marks": 45
        #                 },
        # "record2":{
        #                 "_id": 18,
        #                 "name": "ram",
        #                 "roll_number": 104,
        #                 "branch": "cse",
        #                 "marks": 55
        #             }
        # }
        # # #create collection
        # # collection = mydb['student']
        # # for record in records.values():
        # #     collection.insert_one(record)
        # mylist = [
        #    {
        #                   "_id": 19,
        #                   "name": "john",
        #                   "roll_number": 103,
        #                   "branch": "cse",
        #                   "marks": 45
        #               },
        #    {
        #     "_id": 20,
        #     "name": "jenny",
        #     "roll_number": 108,
        #     "branch": "cse",
        #     "marks": 55
        # },
        #     {
        #         "_id": 21,
        #         "name": "joe",
        #         "roll_number": 105,
        #         "branch": "cse",
        #         "marks": 55
        #     }
        #
        # ]
        #
        # #collection = mydb['student']
        # #collection.insert_many(mylist)
        #
        # # 3 find the  document display document or retreive
        # x = collection.find_one()
        # #print("record", x)
        #
        # # all_document = collection.find()
        # # for each_record in all_document:
        # #     print("doc", each_record)
        #
        # for x in collection.find({}, {"_id":0, "name":1, "branch":1}):
        #     print("Only fields with 1", x)