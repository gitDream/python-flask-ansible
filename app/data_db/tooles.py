import random
from app import db

class utils():

    # 添加数据
    def add_data(self, db, HostAssets, form):
        db.session.add(HostAssets(host_name=form.hostname.data, host_ip=form.ip.data, host_port=form.port.data,
                                  host_user=form.user.data, host_passwrod=form.passwd.data,
                                  host_type=form.systemtype.data))
        db.session.commit()

    # 返回所有数据列表
    def get_all_obj_tables(self, User, info):
        data = []
        db_all_obj = User.query.all()
        for i in range(int(len(db_all_obj))):
            data.append(
                {'name': db_all_obj[i].host_name, 'title': db_all_obj[i].host_ip, 'price': db_all_obj[i].host_port,
                 'number': db_all_obj[i].host_user, 'password': db_all_obj[i].host_type,
                 'time': str(db_all_obj[i].ctime), 'state': int(random.randint(0, 1))})
        limit = info.get('limit', 10)  # 每页显示的条数
        offset = info.get('offset', 0)  # 分片数，(页码-1)*limit，它表示一段数据的起点
        return {'total': len(data), 'rows': data[int(offset):(int(offset) + int(limit))]}

    # 删除某一行列表项
    def del_item(self,str_name,User,db):
        db_id = User.query.filter(User.host_name == str(str_name)).first()
        str_obj=User.query.get(int(db_id.id))
        db.session.delete(str_obj)
        db.session.commit()





    # 批量删除一个集合行列表项
    def del_list_item(self,db,data_list):
        for i in  range(len(data_list)):
            db.session.delete(data_list[i])
            db.session.commit()
        pass

    # 取回一个db列表对象
    def  get_item_obj(self,User,id):
        db_obj=User.query.query.filter(id).first()
        self.id=id
        return db_obj

    #更新一个列表项
    def  update_item(self,User,id):
        db_obj=User.query.query.filter(id).first()
        self.id=id
        return db_obj