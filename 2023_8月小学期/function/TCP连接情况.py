import subprocess

def get_tcp_network_connections():
    try:
        # 执行命令行命令获取网络连接情况
        output = subprocess.check_output(['netstat', '-ano'], text=True)

        # 解析输出，提取IPv4的TCP网络连接情况
        tcp_connections = []
        lines = output.strip().splitlines()
        for line in lines[4:]:
            parts = line.split()
            if len(parts) >= 5 and parts[0] == 'TCP' and '.' in parts[1]:
                local_address = parts[1].split(':')[0]
                foreign_address = parts[2].split(':')[0]
                if local_address != '0.0.0.0' and foreign_address != '0.0.0.0' and local_address != '127.0.0.1' and foreign_address != '127.0.0.1':
                    connection = {
                        'protocol': parts[0],
                        'local_address': parts[1],
                        'foreign_address': parts[2],
                        'state': parts[3],
                        'pid': parts[4]
                    }
                    tcp_connections.append(connection)
        return tcp_connections
    except Exception as e:
        print("获取TCP网络连接情况时出现错误:", str(e))

    return None
