import psutil

"""print('电量、是否在充电:', psutil.sensors_battery())"""


def battery():
    sb = psutil.sensors_battery()
    data = {
        'percent': sb.percent,
        'power_plugged': sb.power_plugged,
        'available_time': round(sb.secsleft/3600, 2),
    }
    if data['available_time'] == -0.0:
        data['available_time'] = '++'
    return data


if __name__ == '__main__':
    print(battery())
    print(psutil.sensors_battery())
