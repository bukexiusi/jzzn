# -*- coding: utf-8 -*-
import json
from sqlalchemy import BigInteger, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class zn_business_table_9(Base):
    __tablename__ = 'zn_business_table_9'

    id = Column(String(18), primary_key=True)
    column1 = Column(String(20))
    column2 = Column(String(20))
    creator = Column(String(20))
    create_time = Column(BigInteger)
    updator = Column(String(20))
    update_time = Column(BigInteger)
    execute_explain = Column(String)
    execute_time = Column(BigInteger)
    execute_duration = Column(Integer)
    batch = Column(String(15))

    def __repr__(self):
        get_data = {
            "id": self.id,
            "column1": self.column1,
            "column2": self.column2,
            "creator": self.creator,
            "create_time": self.create_time,
            "updator": self.updator,
            "update_time": self.update_time,
            "execute_explain": self.execute_explain,
            "execute_time": self.execute_time,
            "execute_duration": self.execute_duration,
            "batch": self.batch,
        }
        get_data = json.dumps(get_data)
        return get_data
