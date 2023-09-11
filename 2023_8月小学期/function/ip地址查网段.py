import ipaddress

"""A类IP地址：范围从1.0.0.0到126.0.0.0；默认子网掩码是255.0.0.0 /8
B类IP地址：范围从128.0.0.0到191.255.0.0；B类IP地址的默认子网掩码是255.255.0.0 /16
C类IP地址：范围从192.0.0.0到223.255.255.0；C类IP地址的默认子网掩码是255.255.255.0 /24"""


def get_network_info(ip_address, subnet_mask):
    try:
        ip_network = ipaddress.IPv4Network(ip_address + '/' + subnet_mask, strict=False)
        num_hosts = ip_network.num_addresses                  # 减去网络地址和广播地址
        is_private = ip_network.is_private
        data = {
            "ip_network": str(ip_network.network_address) + '/' + str(ip_network.prefixlen),
            "num_hosts": num_hosts,
            "is_private": is_private
        }
    except Exception as e:
        data={
            "ip_network": 'null',
            "num_hosts": 'null',
            "is_private": 'null',
        }

    return data

if __name__ == '__main__':

    # 测试示例
    ip = "183.232.231.174"
    subnet_mask = "255.0.0.0"

    info = get_network_info('183.232.231.254', '255.255.0.0')
    print(info)
    print(type(info['is_private']))