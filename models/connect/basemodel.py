#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16
# @Author  : JiaoJianglong


import math

def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class BaseModel(object):

    def create(self,vals,*args,**kwargs):
        """
        在数据库中插入一条记录
        :param vals: 待新建记录的字段值，字典类型
        :return:新建记录的id
        """
        raise NotImplementedError()

    def update(self, vals, *args, **kwargs):
        """
        在数据库中更新一条记录
        :param vals: 待新建记录的字段值，字典类型
        :return:新建记录的id
        """
        raise NotImplementedError()

    def save(self, vals, *args, **kwargs):
        """
        在数据库中插入或保存一条记录
        :param vals: 待新建记录的字段值，字典类型
        :return:新建记录的id
        """
        raise NotImplementedError()

    def search(self,page,page_size,*args,**kwargs):
        """
        查询符合条件的记录
        :param args: 包含检索条件的tuples列表 可用的操作：=,<,>,<=,>=,in,like,ilike,child_of
        :param page:分页索引
        :param page_size:分页大小
        :param context:分页大小
        :return:符合条件记录的id_list
        """
        raise NotImplementedError()

    def read(self,ids,fields=None,*args,**kwargs):
        """
        返回记录的指定字段值列表
        :param ids:待读取的记录的id列表
        :param fields:待读取的字段值,默认读取所有字段
        :return:返回读取结果的字典列表
        """
        raise NotImplementedError()

    def search_read(self,page=1,page_size=10,*args,**kwargs):
        """
        查询符合条件的记录
        :param args: 包含检索条件的tuples列表 可用的操作：=,<,>,<=,>=,in,like,ilike,child_of
        :param page:分页索引
        :param page_size:分页大小
        :param context:分页大小
        :return:符合条件记录的id_list
        """
        raise NotImplementedError()

    def browse(self,select,page,page_size,*args,**kwargs):
        """
        浏览对象及其关联对象
        :param select: 待返回的对象id或id列表
        :param page:
        :param page_size:
        :return:返回对象或对象列表
        """
        raise NotImplementedError()

    def write(self,ids,vals,*args,**kwargs):
        """
        保存一个或几个记录的一个或几个字段
        :param ids:待修改的记录的id列表
        :param vals:待保存的字段新值，字典类型
        :return:如果没有异常，返回True，否则抛出异常
        """
        raise NotImplementedError()

    def unlink(self,ids,*args,**kwargs):
        """
        删除一条或几条记录
        :param ids:待删除记录的id列表
        :return:如果没有异常，返回True，否则抛出异常
        """
        raise NotImplementedError()

    # 计算分页信息
    def count_page(self,length, page, page_size=15, page_show=10):
        page = int(page)
        page_size = int(page_size)
        length = int(length)
        if length == 0:
            return {"enable": False,
                    "page_size": page_size,
                    "skip": 0}
        max_page = int(math.ceil(float(length) / page_size))
        page_num = int(math.ceil(float(page) / page_show))
        pages = list(range(1, max_page + 1)[((page_num - 1) * page_show):(page_num * page_show)])
        skip = (page - 1) * page_size
        if page >= max_page:
            has_more = False
        else:
            has_more = True
        pager = {
            "page_size": page_size,
            "max_page": max_page,
            "pages": pages,
            "page_num": page_num,
            "skip": skip,
            "page": page,
            "enable": True,
            "has_more": has_more,
            "total": length,
        }
        return pager

    # 获取数量
    def get_count(self,query_params):
        """
        获取数量
        :param query_params:
        :return:
        """
        raise NotImplementedError()

