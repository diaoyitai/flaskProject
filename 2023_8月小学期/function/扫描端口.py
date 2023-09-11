import ipaddress
import socket
# 监控网络连接
import time


"""def monitor_network(port):
    # 创建socket连接
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)  # 设置连接超时时间(s)
    try:
        r = s.connect_ex(('220.185.184.26', port))  # 220.185.184.26
        # # 获取连接状态
        # status = s.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
        # print('连接状态:', status)
        # print('远程主机地址：', s.getpeername())  # 远程地址
        # print('本机地址,名称：', s.getsockname(), socket.gethostname(), '\n')  # 主机地址
        # # 关闭连接
        s.close()
        return r

    except Exception as e:
        print(e)
        s.close()
        return 1"""
"""def is_ip_address(address):
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False

def is_domain_name(address):
    if is_ip_address(address):
        return False
    else:
        return True"""

def query_port(ip, port):   #输入ip地址和端口号
    port=int(port)
    s = socket.socket()
    s.settimeout(2)
    try:
        r = s.connect_ex((ip, port))
        s.close()
        if r == 0:
            return '端口开放'
        else:
            return '端口关闭'
    except Exception as e:
        s.close()
        return 'IP错误！'


if __name__ == '__main__':
    # 定时执行监控任务
    # while True:
    #     monitor_network()
    #     time.sleep(3)  # 每3秒执行一次
    "服务器常用默认端口号"
    # port_numbers = [21, 22, 23, 25, 53, 69, 80, 3128, 110, 119, 123, 135, 137, 138, 139, 161, 389,
    #                 443, 465, 873, 1080, 1158, 1433, 1521, 2100, 3389, 3306, 5432, 5601, 6379, 8080, 8081, 8888, 9000,
    #                 9080, 9090, 9200, 10050, 10051, 11211, 27017, 22122]
    #
    # for port in port_numbers:
    #     if monitor_network(port) == 0:
    #         print("Port:", port, '打开')
    #     else:
    #         print("Port:", port, '关闭')
    print(query_port('10.225.205.53', 80))

