from datetime import datetime
from App.models import User, Advice, Power
import psutil
from flask import request, session
from flask_restful import Resource
from App.exts import db
from function.ip地址查网段 import get_network_info
from function.ip查询 import domain_ip
from function.所有进程 import proc
from function.扫描端口 import query_port
from function.操作系统类型 import operating_system
from function.电池信息 import battery
from function.磁盘 import disk
from function.系统启动时间 import get_system_boot_time
from function.系统用户 import user_name
from function.网络接收发送 import recv_sent
from function.TCP连接情况 import get_tcp_network_connections
from function.内存信息 import svmem, swap


class ip(Resource):  # ip查询
    def post(self):
        return domain_ip(request.form.get('domain'))


class port(Resource):
    def post(self):
        ip = request.form.get('ip')
        port = request.form.get('port')
        print(ip, port)
        print(type(ip))
        return query_port(ip, port)


class network_segment(Resource):
    def post(self):
        ip = request.form.get('ip')
        mask = request.form.get('mask')
        print(ip, mask)
        print(type(ip), type(mask))
        return get_network_info(ip, mask)


# 处理登录请求
class login(Resource):
    def post(self):
        a = request.form.get('account')
        p = request.form.get('password')
        print(a, p, '有人登录')
        u = User.query.filter(User.account == a, User.password == p).first()  # 检索是否有这名用户
        if u:  # 有这名用户
            print('有这名用户')
            session['state'] = True  # 登录状态变true
            session['account'] = u.account  # flask_session存储用户账号 用户类型
            session['type'] = u.type
            return [True, u.account]

        return [False]


# 处理退出登录请求
class exit(Resource):
    def get(self):
        session.clear()  # 清空存储在服务器的session的键值
        return True


# 处理注册请求
class register(Resource):
    def post(self):
        a = request.form.get('account')
        p = request.form.get('password')
        print(a, p)
        data = {  # 返回给前端的信息
            'state': False,
            'error': '',
        }
        u = User.query.filter(User.account == a).first()
        if u:  # 账号已存在
            data['error'] = '账号已存在'
            return data
        else:
            try:
                newUser = User(account=a, password=p)
                print(newUser)
                db.session.add(newUser)  # 添加新用户
                db.session.commit()
                data['state'] = True
            except Exception as e:  # 如果数据库出错
                print('用户注册账号出错！')
                db.session.rollback()  # 回滚
                db.session.flush()  # 刷新
                data['error'] = str(e)  # 返回错误信息

        return data


# 返回系统信息
class sys_info(Resource):
    def get(self):
        data = {
            'type': operating_system(),  # 操作系统类型
            'user': user_name(),  # 用户名主机名
            'start': get_system_boot_time(),  # 系统启动时间
            'battery': battery(),  # 电池
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        return data


# 返回磁盘信息
class disk_info(Resource):
    def get(self):
        data = disk()
        data['time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return data


class CPU_info(Resource):
    def get(self):
        used = []
        for x in range(5):
            used.append(psutil.cpu_percent(interval=0.4, percpu=False))
        data = {
            '逻辑处理器': psutil.cpu_count(logical=True),
            '内核': psutil.cpu_count(logical=False),
            'used': used
        }
        return data


class network(Resource):
    def get(self):
        Data = {
            'r_s': recv_sent(),
            'tcp': get_tcp_network_connections()
        }
        return Data


class memory_info(Resource):
    def get(self):
        return {
            'svmem': svmem(),
            'swap': swap(),
        }


class process_info(Resource):
    def get(self):
        return proc()


# 用户建议
class advice(Resource):
    def get(self):
        E = request.args.get("E")
        C = request.args.get("c")
        try:
            new_advice = Advice(Email=E, content=C)
            db.session.add(new_advice)
            db.session.commit()
            return True
        except Exception as e:
            print(e, '用户提交建议出错了！')
            db.session.rollback()
            db.session.flush()
            return False


# 提升权限
class power(Resource):
    def post(self):
        p = request.form.get('power')
        a = session['account']
        u = User.query.filter(User.account == a, ).first()
        t = Power.query.filter(Power.power == p).first()
        if t:
            try:
                # 删除验证码
                db.session.delete(t)
                u.type = '管理员'
                # 退出登录
                session.clear()
                return True
            except Exception as e:
                db.session.rollback()
                db.session.flush()
                print('提升权限失败')
                return False
        else:
            return False
