from flask import Flask
from App.exts import init_exts
from App.views import blue
from .urls import *
# from App.models import User      在api那导了包

def create_app():
    app=Flask(__name__)
    #注册蓝图
    app.register_blueprint(blueprint=blue)

    #配置session
    app.config['SECRET_KEY']='abc123'#密钥 session加密要用到的字符串 必须配置

    #配置数据库
    db_uri ='mysql+pymysql://root:admin@localhost:3306/network monitoring system'

    app.config['host']='0.0.0.0'
    app.config['port']=80
    app.config['SQLALCHEMY_DATABASE_URI']=db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False  # 禁止对象追踪修改以提高性能
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # 设置自动提交 在每个请求结束时，Flask会自动调用db.session.commit()来提交会话中的更改，确保更改被永久保存到数据库。
    #插件绑定
    init_exts(app)
    return app