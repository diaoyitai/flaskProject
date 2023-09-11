import psutil


# print('挂载信息(C盘、D盘):',psutil.disk_partitions())
"""
print('D盘使用信息:',psutil.disk_usage('D:\\'))
print('C盘使用信息:',psutil.disk_usage('C:\\'))
print('io统计(字节,毫秒)',psutil.disk_io_counters(perdisk=False, nowrap=True))#读取、写入次数等等等"""
def memory(type):       #单位转换成GB
    v = type
    data = {
        'total': round(v.total / (1024 * 1024*1024), 2),
        'used': round(v.used / (1024 * 1024*1024), 2),
        'free': round(v.free / (1024 * 1024*1024), 2),
        'percent': v.percent,
    }
    return data

def disk():
    data = {
        'C': memory(psutil.disk_usage('C:\\')),
        'D': memory(psutil.disk_usage('D:\\')),
        'E': memory(psutil.disk_usage('E:\\'))
    }
    return data


if __name__ == '__main__':
    print(disk())
