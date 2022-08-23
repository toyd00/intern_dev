import argparse
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Boolean
import sqlalchemy.ext.declarative
import sqlalchemy.orm




engine = sqlalchemy.create_engine('mysql+pymysql://root:sekigahara@127.0.0.1/test_database')
#engine = sqlalchemy.create_engine('sqlite:///:memory]')

Base = sqlalchemy.ext.declarative.declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = sqlalchemy.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(50), nullable=False)
    email_adress = Column(String(50), nullable=False)
    password = Column(String(200), nullable=False)
    is_manager = Column(Boolean, nullable=False)
    is_deleted = Column(Boolean, nullable=False)
    note = Column(String(400),nullable=True)

class UserGroup(Base):
    __tablename__ = 'usergroups'
    id = sqlalchemy.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    parent_usergroup_id = Column(Integer, nullable=False)
    group_name = Column(String(50), nullable=False)
    is_deleted = Column(Boolean, nullable=False)
    note = Column(String(400),nullable=True)

class Device(Base):
    __tablename__ = 'devices'
    id = sqlalchemy.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    device_name = Column(String(50), nullable=False)
    is_deleted = Column(Boolean, nullable=False)
    note = Column(String(400),nullable=True)

class DeviceGroup(Base):
    __tablename__ = 'devicegroups'
    id = sqlalchemy.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    parent_devicegroup_id = Column(Integer, nullable=False)
    group_name = Column(String(50), nullable=False)
    is_deleted = Column(Boolean, nullable=False)
    note = Column(String(400),nullable=True)

class UserDevice(Base):
    __tablename__ = 'users_devices'
    id = sqlalchemy.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id',onupdate='CASCADE', ondelete='CASCADE'))
    device_id = Column(Integer, ForeignKey('devices.id',onupdate='CASCADE', ondelete='CASCADE'))

class UserUserGroup(Base):
    __tablename__ = 'users_usergroups'
    id = sqlalchemy.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id',onupdate='CASCADE', ondelete='CASCADE'))
    usergroup_id = Column(Integer, ForeignKey('usergroups.id',onupdate='CASCADE', ondelete='CASCADE'))

class DeviceDeviceGroup(Base):
    __tablename__ = 'devices_devicegroups'
    id = sqlalchemy.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    device_id = Column(Integer, ForeignKey('devices.id',onupdate='CASCADE', ondelete='CASCADE'))
    devicegroup_id = Column(Integer, ForeignKey('devicegroups.id',onupdate='CASCADE', ondelete='CASCADE'))

class UserGroupDeviceGroup(Base):
    __tablename__ = 'usergroups_devicegroups'
    id = sqlalchemy.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    usergroup_id = Column(Integer, ForeignKey('usergroups.id',onupdate='CASCADE', ondelete='CASCADE'))
    devicegroup_id = Column(Integer, ForeignKey('devicegroups.id',onupdate='CASCADE', ondelete='CASCADE'))



Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()


