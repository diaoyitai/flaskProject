import json
from flask import Blueprint, request, render_template, Response, redirect, url_for, session, g

# 蓝图
blue = Blueprint('user', __name__)


@blue.route('/')
def index():
    if 'state' not in session:
        session['state'] = False  # 登录状态
    return render_template('主页面.html')


@blue.route('/demo1/')
def demo1():
    return render_template('demo1.html')


@blue.route('/demo2/')
def demo2():
    return render_template('demo2.html')


@blue.route('/demo3/')
def demo3():
    return render_template('demo3.html')


# 查ip
@blue.route('/Service1/')
def Service1():
    if not session['state']:  # 如果在没有登录的情况下输入url访问，返回错误页面
        return redirect('/fail')

    return render_template('Service1.html')


# 查端口
@blue.route('/Service2/')
def Service2():
    if not session['state']:
        return redirect('/fail')
    return render_template('Service2.html')


# 查域名（地图）
@blue.route('/Service3/')
def Service3():
    if not session['state']:
        return redirect('/fail')
    return render_template('Service3.html')


# 查网段
@blue.route('/Service4/')
def Service4():
    if not session['state']:
        return redirect('/fail')
    return render_template('Service4.html')


@blue.route('/fail/')
def fail():
    return render_template('fail.html')


# 注册
@blue.route('/register/')
def register():
    return render_template('register.html')


# 主机监控页面
@blue.route('/host/')
def host():
    if not session['state']:
        return redirect('/fail')
    return render_template('host_status.html')
