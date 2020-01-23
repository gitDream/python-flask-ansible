from app import app ,db ,manager

#初始创表
@manager.command
def create_tab():
    print("create_Mysql_tab")
    db.create_all()


#初始删表
@manager.command
def drop_tab():
    print("delect_Mysql_tab")
    db.drop_all()



if __name__ == '__main__':
    manager.run()