#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 0016 19:28
# @Author  : jiaojianglong




from sqlalchemy import create_engine
from setting import MYSQL_INFO
from models.mysql.test import Base  #新建哪的table就要引入哪的


if __name__ == "__main__":
    engine = create_engine(MYSQL_INFO)
    Base.metadata.create_all(engine)
