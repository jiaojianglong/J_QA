#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 0016 19:19
# @Author  : jiaojianglong


from models.connect.basemodel import BaseModel
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mongodb = myclient["j_qa"]
# dblist = myclient.list_database_names()#所有数据库
# collist = mongodb. list_collection_names()#数据库中所有集合


class MongoDB(BaseModel):

    def __init__(self):
        print(self.name)
        self.mydb = myclient[self.name.split(".")[0]]
        self.mycol = self.mydb[self.name.split(".")[1]]

    def create(self, vals, *args, **kwargs):
        x = self.mycol.insert_one(vals,args,kwargs)

    def update(self, vals, *args, **kwargs):
        pass

    def search(self,page,page_size,*args,**kwargs):
        pass
