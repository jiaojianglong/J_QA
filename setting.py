#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 21:56
# @Author  : jiaojianglong



#clients = [dict(host="114.115.175.100",send_port=8899,accept_port=8898,name="华为云")]
clients = [dict(host="127.0.0.1",send_port=8899,accept_port=8898,name="本地")]


MYSQL_INFO = "mysql+pymysql://root:123456@localhost:3306/model"

ES_CONN_INFO = {"hosts":['localhost', 'otherhost'],
                "http_auth":('user', 'secret'),
                "scheme":"https",
                "port":443,
                "timeout":240}