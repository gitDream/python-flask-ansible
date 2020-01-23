import sys , importlib ,time
from uuid import uuid4
from sqlalchemy.ext import declarative
from app import db

#from jmilkfansblog.extensions import bcrypt, cache

# Fix the BUG:
#    UnicodeEncodeError: 'ascii' codec can't encode characters in position
# TS: Set the system encoding to utf-8(support chinese)
# Q: Why need to reload the sys module?
# A: System will be deleted the sys.setdefaultencoding after imported the
#    site.py. So, we have to reload the sys module and reset the default
#    encoding again
importlib.reload(sys)


# Create the db object
# Init the db from jmilkfansblog/__init__py

# SQLAlchemy Base
Base = declarative.declarative_base()


class HostAssets(db.Model):
    """Represents Proected users."""

    # Set the name for table
    __tablename__ = 'assets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)   # id 整型，主键，自增，唯一
    host_name = db.Column(db.String(255),nullable=False)
    host_ip = db.Column(db.String(255),nullable=False)
    host_port = db.Column(db.String(64),nullable=False)
    host_user = db.Column(db.String(255),nullable=False)
    host_passwrod = db.Column(db.String(255),nullable=False)
    ctime = db.Column(db.DateTime, default=time.strftime('%Y-%m-%d %H:%M:%S'))
    host_type = db.Column(db.String(64),nullable=False)


    def __init__(self, host_name, host_ip,host_port,host_user,host_passwrod,host_type):
        self.host_name = host_name
        self.host_ip = host_ip
        self.host_port = host_port
        self.host_user = host_user
        self.host_passwrod = host_passwrod
        self.host_type = host_type

    def __repr__(self):
        """Define the string format for instance of User."""
        return "<Model User `{}`>".format(self.host_name)

if __name__ == '__main__':
#    #启动webssh
    pass


