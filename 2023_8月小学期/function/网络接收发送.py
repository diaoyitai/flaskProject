import psutil
import socket
import subprocess

"""a = psutil.net_io_counters(pernic=False, nowrap=True)
print(a)
print(round(a.bytes_sent / (1024 * 1024), 2))
print(round(a.bytes_recv / (1024 * 1024), 2))"""


def get_local_ip():
    ip_list = []
    hostname = socket.gethostname()
    addrinfo = socket.getaddrinfo(hostname, None)

    for addr in addrinfo:
        ip = addr[4][0]
        if ip not in ip_list:
            ip_list.append(ip)
    return ip_list


def recv_sent():
    ip_data = get_local_ip()  # 获取本机全部IP地址  ipv4/ipv6
    ipv4=[]
    for ip in ip_data:
        if '.'in ip:
            ipv4.append(ip)
    a = psutil.net_io_counters(pernic=False, nowrap=True)
    data = {
        'ip': ipv4,
        'recv': round(a.bytes_recv / (1024 * 1024), 2),  # 单位：MB
        'sent': round(a.bytes_sent / (1024 * 1024), 2),
    }
    return data


# ip_address = socket.gethostbyname(socket.gethostname())
# print("IP 地址:", ip_address)
#
# port_status = subprocess.check_output(['netstat', '-ano'])
# print("端口状态:", port_status.decode('gbk'))
# mac_address = subprocess.check_output(['getmac']).decode('gbk')
# print("MAC 地址:", mac_address)
if __name__ == '__main__':
    print(recv_sent())
    print(socket.gethostbyname(socket.gethostname()))
