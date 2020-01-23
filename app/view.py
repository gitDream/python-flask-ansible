from flask import render_template,redirect,json,url_for ,request ,jsonify
from app import app ,db
from  .wtf_flask.CreateHost import AssetsHost
from .data_db.tooles import utils
from .data_db.models import HostAssets

#index
@app.route('/', methods = ['GET', 'POST'])
def index():
    form=AssetsHost()
    if request.method == 'POST':
        return  "ERROR_404"
    elif request.method == 'GET':
      return   render_template("web_service/index.html",form=form)
    return  "ERROR_404"

#show data
@app.route('/tables/data',methods=['GET','POST'])
def show_tables():
    if request.method == 'POST':
        return "Error 404"
    elif request.method == 'GET':
        data = utils().get_all_obj_tables(User=HostAssets,info = request.values)
    return jsonify(data)


#delete data
@app.route('/tables/delitem',methods=['GET','POST'])
def del_item():
    if request.method == 'POST':
        #先要验证客户端Session与Cookie 是否配对才给删数据  这我就不写了
        item_name=request.values.get("item_name")
        utils().del_item(db=db,str_name=item_name,User=HostAssets)
    elif request.method == 'GET':
        return "ERROR_404"
    return "ERROR_404"

#add data
@app.route('/addhost',methods=['GET','POST'])
def add_host():
    # 创建表单对象AssetsHost
    form=AssetsHost()
    if request.method == "POST":
    # 判断是否是有效的提交
        if form.validate_on_submit():
            utils().add_data(HostAssets=HostAssets,db=db,form=form)
            return redirect(url_for('index'))
    elif request.method == "GET":
        return "Error 404"
    return   "Error 404"


if __name__ == '__main__':
    pass
