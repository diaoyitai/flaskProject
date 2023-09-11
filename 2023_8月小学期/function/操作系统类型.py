import psutil


def operating_system():
    data = '其他'
    if psutil.LINUX:
        data = 'LINUX'
    elif psutil.WINDOWS:
        data = 'WINDOWS'
    elif psutil.MACOS:
        data = 'MACOS'
    return data


if __name__ == '__main__':
    print(operating_system())