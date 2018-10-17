#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 0016 19:19
# @Author  : jiaojianglong


from models.connect.basemodel import BaseModel
import pymongo
import datetime
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mongodb = myclient["j_qa"]
# dblist = myclient.list_database_names()#所有数据库
# collist = mongodb. list_collection_names()#数据库中所有集合


class MongoDB(BaseModel):

    def __init__(self,name):
        self.name = name
        self.mydb = myclient[self.name.split(".")[0]]
        self.coll = self.mydb[self.name.split(".")[1]]

    def create(self, vals, *args, **kwargs):
        curr_time = str(datetime.datetime.now())
        vals["create_date"] = curr_time
        vals["write_date"] = curr_time
        vals["is_enable"] = True

        vals["maintain"] = [dict(
            operation_time=curr_time,
            operation_type="create",
        )]
        self.coll.insert_one(vals)
        return

    def update(self, vals, *args, **kwargs):
        query_params = kwargs.get("query_params") or {}
        if not query_params:
            raise Exception("查询参数不能为空！")

        count = self.get_count(query_params)
        if count != 1:
            raise Exception("需要更新的数据个数：%s, 查询条件错误：%s！" % (count, query_params))

        query_params.update(dict(
            is_enable=True,
        ))
        cr = self.coll.find(query_params)
        curr_date = str(datetime.datetime.now())

        if not vals:
            raise Exception("更新内容不能为空！")

        vals.update(dict(
            write_date=curr_date,
        ))
        for obj in cr:
            obj.update(vals)
            obj["maintain"] = obj.get("maintain") or []
            obj["maintain"].append(dict(
                operation_time=curr_date,
                operation_type="update",
            ))
            obj["maintain"] = obj["maintain"][:1] + obj["maintain"][-1:]
            self.coll.save(obj)
        return self.coll.find_one(query_params)

    def search(self,page,page_size,*args,**kwargs):
        pass

    def find_one(self, *args, **kwargs):
        # 检查查询参数
        if not "query_params" in kwargs:
            raise Exception("查询参数query_params不存在！")
        if not isinstance(kwargs.get("query_params"), dict):
            raise Exception("查询参数query_params:%s, 类型错误！" % kwargs.get("query_params"))
        if not kwargs.get("query_params"):
            raise Exception("查询参数query_params:%s, 不能为空！" % kwargs.get("query_params"))

        # 查询参数
        query_params = kwargs.get("query_params")
        query_params.update(dict(
            is_enable=True,
        ))
        obj = self.coll.find_one(query_params)
        if not obj:
            raise Exception("不存在:%s！" % query_params)
        return obj

    def get_count(self, query_params):
        print(self.coll.count(query_params))
        return self.coll.count(query_params)