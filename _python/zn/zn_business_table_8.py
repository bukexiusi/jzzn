# -*- coding: utf-8 -*-
import json
from sqlalchemy import BigInteger, Column, Integer, SmallInteger, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class zn_business_table_8(Base):
    __tablename__ = 'zn_business_table_8'

    id = Column(String(18), primary_key=True)
    column1 = Column(String(20), nullable=False)
    column2 = Column(String(20))
    column3 = Column(String(20))
    column4 = Column(String(20))
    column5 = Column(String(20))
    column6 = Column(String(20))
    column7 = Column(String(20))
    column8 = Column(String(20))
    column9 = Column(String(20))
    column10 = Column(String(20))
    column11 = Column(String(20))
    column12 = Column(String(20))
    column13 = Column(BigInteger)
    column14 = Column(BigInteger)
    column15 = Column(String(20))
    column16 = Column(String(20))
    column17 = Column(String(20))
    column18 = Column(BigInteger)
    creator = Column(String(20))
    create_time = Column(BigInteger)
    updator = Column(String(20))
    update_time = Column(BigInteger)
    execute_explain = Column(String)
    execute_time = Column(BigInteger)
    execute_duration = Column(Integer)
    batch = Column(String(15))
    column_add_92 = Column(SmallInteger)

    def __repr__(self):
        get_data = {
            "id": self.id,
            "column1": self.column1,
            "column2": self.column2,
            "column3": self.column3,
            "column4": self.column4,
            "column5": self.column5,
            "column6": self.column6,
            "column7": self.column7,
            "column8": self.column8,
            "column9": self.column9,
            "column10": self.column10,
            "column11": self.column11,
            "column12": self.column12,
            "column13": self.column13,
            "column14": self.column14,
            "column15": self.column15,
            "column16": self.column16,
            "column17": self.column17,
            "column18": self.column18,
            "creator": self.creator,
            "create_time": self.create_time,
            "updator": self.updator,
            "update_time": self.update_time,
            "execute_explain": self.execute_explain,
            "execute_time": self.execute_time,
            "execute_duration": self.execute_duration,
            "batch": self.batch,
            "column_add_92": self.column_add_92,
        }
        get_data = json.dumps(get_data)
        return get_data
