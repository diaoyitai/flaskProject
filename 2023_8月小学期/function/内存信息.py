import psutil

"""print('运行内存(字节):', psutil.virtual_memory())  # 总   可分配的    已使用百分比  正在使用的   空闲的        Windows上可分配的==空闲的
print('交换内存信息:', psutil.swap_memory())
p = psutil.virtual_memory()
print(p.total / (1024 * 1024), 'MB')
print(round(p.total / (1024 * 1024), 2))
"""


def memory(type):
    v = type
    data = {
        'total': round(v.total / (1024 * 1024), 2),
        'used': round(v.used / (1024 * 1024), 2),
        'free': round(v.free / (1024 * 1024), 2),
        'percent': v.percent,
    }
    return data


def svmem():  # 单位：MB
    return memory(psutil.virtual_memory())


def swap():
    return memory(psutil.swap_memory())


if __name__ == '__main__':
    print(svmem())
    print(swap())
