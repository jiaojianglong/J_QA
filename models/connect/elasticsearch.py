#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/21 0021 10:49
# @Author  : jiaojianglong


from models.connect.basemodel import BaseModel
from setting import ES_CONN_INFO
import elasticsearch
from elasticsearch import helpers

es_conn = elasticsearch.Elasticsearch(ES_CONN_INFO)

class ES():

    def __init__(self,index,type):
        self._index = index
        self._type = type

    def create(self,body,id=None,refresh=False):
        """
        新建一条数据
        :param body: 数据内容
        :param id: 指定新建数据的id
        :param refresh: 是否刷新使文档可被搜索“true”、“false”、“wait_for”
        :return:
        """
        return es_conn.create(index=self._index,doc_type=self._type,body=body,id=id,refresh=refresh)

    def index(self,body,id=None,refresh=False):
        """
        添加或更新类型化JSON文档，使其可搜索
        :param body:文档内容
        :param id:指定文档id
        :param refresh:是否刷新
        :return:
        """
        return es_conn.index(index=self._index,doc_type=self._type,body=body,id=id,refresh=refresh)

    def search(self,body,_source=True,page=0,size=10,page_flag=True):
        """
        通过查询语句来获取文档
        :param body: 查询语句
        :param _source: 返回的字段
        :param page: 指定查询返回结果的页数
        :param size: 指定每页文档数量
        :param page_flag: 是否使用分页，如果否则返回所有满足的文档
        :return: 查询结果
        """
        if page_flag:
            from_=page*size
            return es_conn.search(index=self._index,doc_type=self._type,body=body,_source=_source,from_=from_,size=size)
        else:
            return helpers.scan(client=es_conn,query=body,scroll="2m",index=self._index,doc_type=self._type,_source=_source)

    def get_count(self,query):
        """
        执行查询并获取该查询的匹配数
        :param body:查询语句
        :return:count
        """
        return es_conn.count(index=self._index,doc_type=self._type,body=query)

    def update(self,body,id):
        """
        更新文档
        :param body: 要更新的部分
        :param id:要更新的文档id
        :return:
        """
        return es_conn.update(index=self._index,doc_type=self._type,body=body,id=id)

    def delete(self,id):
        """
        删除指定id的数据
        :param id: 要删除数据的id
        :return:
        """
        return es_conn.delete(index=self._index,doc_type=self._type,id=id)

    def delete_by_query(self,query):
        es_conn.delete_by_query(index=self._index,doc_type=self._type,body=query)

    def exists(self,id,refresh=True):
        """
        查看是否有给定的id
        :param id: 文档的id
        :param refresh: 在执行操作之前刷新包含文档的碎片
        :return: False,True
        """
        return es_conn.exists(index=self._index,doc_type=self._type,id=id,refresh=refresh)

    def explain(self,id,body):
        """
        计算 查询和特定文档 的得分解释。无论文档是否匹配特定查询，这都可以提供有用的反馈
        :param id:要查询文档的id
        :param body:查询语句
        :return:反馈结果
        """
        return es_conn.explain(index=self._index,doc_type=self._type,id=id,body=body)

    def get(self,id,_source=True,refresh=False):
        """
        获取指定id的文档
        :param id: 要获取文档的id
        :param _source: 是否返回_source,或者指定要返回字段的list
        :param refresh: 查询前是否刷新
        :return: 获取到的文档
        """
        return es_conn.get(index=self._index,doc_type=self._type,id=id,_source=_source,refresh=refresh)

    def mget(self,ids,_source=True):
        """
        一次获取多个给定id的文档
        :param ids: 要获取文档的id
        :param _source: 返回字段
        :return:
        """
        return es_conn.mget(index=self._index,doc_type=self._type,body=ids,_source=_source)

    def get_source(self,id,_source=True,refresh=False):
        """
        通过索引、类型和id获取文档的源
        :param id:文档id
        :param _source:要返回的字段
        :param refresh:查询前是否更新
        :return:获取到的source
        """
        return es_conn.get_source(index=self._index,doc_type=self._type,id=id,_source=_source,refresh=refresh)


