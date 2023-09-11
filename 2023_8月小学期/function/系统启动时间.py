import datetime
import psutil
import pytz


def get_system_boot_time():
    boot_time = psutil.boot_time()
    utc_boot_time = datetime.datetime.utcfromtimestamp(boot_time)
    local_tz = pytz.timezone('Asia/Shanghai')  # 设置本地时区，根据实际情况修改
    local_boot_time = utc_boot_time.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_boot_time.strftime("%Y-%m-%d %H:%M:%S")
if __name__ == '__main__':
    print(get_system_boot_time())