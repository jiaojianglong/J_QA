



from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from setting import MYSQL_INFO
from models.connect.basemodel import BaseModel


engine = create_engine(MYSQL_INFO)
DBSession = sessionmaker(bind=engine)


class MySQL(BaseModel):

    def __init__(self,__db__):
        self.__db__ = __db__
        self.session = DBSession()

    def create(self,*args,**kwargs):
        """
        在数据库插入一条新数据
        :param args:
        :param kwargs:
        :return: 新插入数据的id
        """
        new_user = self.__db__(*args,**kwargs)
        self.session.add(new_user)
        self.session.commit()
        self.session.close()
        return new_user

    @classmethod
    def update_by_id(cls, id, date):
        """
        在数据库中更新一条记录
        :param vals: 待新建记录的字段值，字典类型
        :return:新建记录的id
        """
        try:
            session = DBSession()
            target = session.query(cls).filter(cls.id == id).first()
            for key,value in date.items():
                target.__setattr__(key,value)
            session.commit()
            session.close()
        except Exception as e:
            print("程序报错",e.args)


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

    # 获取数量
    def get_count(self,query_params):
        """
        获取数量
        :param query_params:
        :return:
        """
        raise NotImplementedError()




