from datetime import datetime

from App.exts import db


# flask db init 创建迁移文件夹migrates，只调用一次
# flask db migrate 生成迁移文件
# flask db upgrade执行迁移文件中的升级
# flask db downgrade 执行迁移文件中的降级
# flask db stamp head是一个数据库迁移命令，用于将数据库迁移历史记录标记为最新的迁移版本。

# 用户表
# id 账号 密码 用户类型 注册时间
class User(db.Model):
    # 表名
    __tablename__ = 'user'
    # 定义表字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, )  # autoincrement自动递增  Column列
    account = db.Column(db.String(11), unique=True)
    password = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(3), default='普通')  # 管理员/普通
    join_time = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class Advice(db.Model):
    # 表名
    __tablename__ = 'advice'
    # 定义表字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, )  # autoincrement自动递增  Column列
    Email = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(9999), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class Power(db.Model):
    # 表名
    __tablename__ = 'power'
    # 定义表字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, )  # autoincrement自动递增  Column列
    power = db.Column(db.String(100), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
