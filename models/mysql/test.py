#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16
# @Author  : JiaoJianglong

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from models.connect.mysql import MySQL


Base = declarative_base()


class User(Base,MySQL):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))



#Base.metadata.create_all(engine)

#User.create(id=3,name="jiao")
User.update_by_id(id=3,name="hahaha")
