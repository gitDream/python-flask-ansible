# 导入表单类的基类
from flask_wtf import FlaskForm
# 导入字段类型
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, IntegerField,FileField
from wtforms.validators import Length, Regexp, DataRequired,NumberRange,IPAddress
from flask_wtf.file import FileField,FileAllowed,FileRequired
#请注意，如果要在FileField中加上FileAllowed等验证函数的话，就不能从wtforms中导入Field类，而是必须从flask_wtf.file中，否则会报错没有has_file方法。
from .UPloadSet import UploadSet

# 创建表单类
myfile = UploadSet('MYFILE')

#上传得脚本
class FileRole(FlaskForm):
    # name = StringField('用户名')
    # submit = SubmitField('提交')
    filename = StringField('脚本名:', validators=[Length(3, 6, message='脚本名必须是3~6个字符')])
    fileobject= FileField('请选择文件:',validators=[FileAllowed(myfile,u'文件格式不对'),FileRequired()])
    submit = SubmitField('上传')

#添加系统主机
class AssetsHost(FlaskForm):
    hostname = StringField('系统命名:')
    ip = StringField('主机ip:', validators=[DataRequired(message='请输入：主机IP'),Length(10,20, message='ip：10.10.10.1'), IPAddress(ipv4=True)])
    port = StringField('端口:', validators=[DataRequired(message='请输入：主机端口'),Length(min=1, max=5, message='主机端口：2-5位')])
    user = StringField('登陆用户:', validators=[DataRequired(message='请输入：用户'), Length(3, 60)])
    passwd = PasswordField('登陆密码:', validators=[DataRequired(message='请输入：密码'), Length(6, 20)])
    systemtype = SelectField(
        label='系统类型',
        validators=[DataRequired('帮你选了Centos')],
        render_kw={
            'class': 'form-control'
        },
        choices=[('Centos-7', 'Centos-7'), ('Redhat-7', 'Redhat-7')],
        default = 'Centos-7',
        coerce=str
    )
    #点击保存按钮
    submit = SubmitField("添加")
