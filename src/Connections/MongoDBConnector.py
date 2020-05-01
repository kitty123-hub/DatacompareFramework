import urllib
import pymongo
import sys

class MongoDBConnector:
    @classmethod
    def DbConnect(cls,UserName,host,port,Password):
        mongoHost = host#cls.readSetting("Mongo", "Host", cls.default['mongoHost'])
        mongoPort = port#cls.readSetting("Mongo", "Port", cls.default['mongoPort'])
        #mongoDB = MongoDB#cls.getMongoDB()
        mongoUsername = str(UserName)#cls.readSetting("Mongo", "Username", cls.default['mongoUsername'])
        mongoPassword = str(Password)#cls.readSetting("Mongo", "Password", cls.default['mongoPassword'])

        mongoUsername = urllib.parse.quote(mongoUsername)
        print (mongoUsername)
        mongoPassword = urllib.parse.quote(mongoPassword)
        print(mongoPassword)
        try:
            if mongoUsername and mongoPassword:
                mongoURI = "mongodb://{username}:{password}@{host}:{port}/".format(
                    username=mongoUsername, password=mongoPassword,
                    host=mongoHost, port=mongoPort

                )
                #connect = pymongo.MongoClient(mongoURI, connect=False)
                connect = pymongo.MongoClient(mongoURI,connect=False)
                #print ("entry1")

            else:
                #mongoURI = "mongodb://{host}:{port}/".format(
                #    username=mongoUsername, password=mongoPassword,
                #    host=mongoHost, port=mongoPort
                #)
                connect = pymongo.MongoClient(mongoHost, mongoPort, connect=False)
                #print("entry2")
            #connect = pymongo.MongoClient(mongoURI)
        except:
            sys.exit("Unable to connect to Mongo. Is it running on %s:%s?" % (mongoHost, mongoPort))
        return connect