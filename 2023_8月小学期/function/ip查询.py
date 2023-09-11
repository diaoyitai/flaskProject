import socket

# 用域名查ip
# i = socket.gethostbyname('123')
# print(i)


def domain_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except Exception as e:
        print(e)
        return 'Null'

if __name__ == '__main__':
    print(domain_ip('123'))
