#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 0016 19:57
# @Author  : jiaojianglong
from models.connect.mongodb import MongoDB



class EmoticonModel(MongoDB):
    name = "j_qa.emoticon"
    column = ["content","url","group","replys",""]

