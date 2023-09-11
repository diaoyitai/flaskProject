import socket

import psutil


def user_name():
    data={
        'user': psutil.users()[0].name,
        'name': socket.gethostname()
    }
    return data

if __name__ == '__main__':
    print(user_name())
