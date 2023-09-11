from .exts import api
from .apis import *

api.add_resource(ip, '/ip/')  # ip查询
api.add_resource(port, '/port/')  # 查端口
api.add_resource(network_segment, '/Network_segment/')  # 查网段
# 处理登录请求
api.add_resource(login, '/login/')
# 退出登录请求
api.add_resource(exit, '/exit/')
# 注册
api.add_resource(register, '/register_request/')

# 返回系统信息
api.add_resource(sys_info, '/host/sys_info/')
# 返回磁盘信息（C D E）
api.add_resource(disk_info, '/host/disk_info/')
# 返回cup利用率信息
api.add_resource(CPU_info, '/host/cpu_info/')
# 网络情况
api.add_resource(network, '/host/network/')
# 内存信息
api.add_resource(memory_info, '/host/memory_info/')
# 返回所有正在运行的进程
api.add_resource(process_info, '/host/process_info/')
#用户建议
api.add_resource(advice, '/advice/')
#提权
api.add_resource(power, '/power/')
