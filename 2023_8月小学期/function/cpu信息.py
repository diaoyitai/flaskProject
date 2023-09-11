import time
import psutil

"""print('cpu在各个模式的运行时间(s):',psutil.cpu_times(percpu=False)) #打印cpu在各个模式的运行时间(s)   12个
print('cup 平均利用率:',psutil.cpu_percent(interval=0.5, percpu=True))#1秒间隔内cup 利用率
print('cpu耗时比例:',psutil.cpu_times_percent(interval=1, percpu=False))#1秒间隔内cpu各个模式的 时间利用率
print('逻辑处理器数量:',psutil.cpu_count(logical=True))
print('内核数量：',psutil.cpu_count(logical=False))
print('cpu当前频率，最小频率，最大频率(Mhz)：',psutil.cpu_freq(percpu=False))"""


def cpu_utilization():  # 利用率
    return psutil.cpu_percent(interval=0.5, percpu=False)


def cpu_logical_processors_num():  # 逻辑处理器数量
    return psutil.cpu_count(logical=True)


def cpu_cores_num():  # 内核数量
    return psutil.cpu_count(logical=False)


if __name__ == '__main__':
    pass

