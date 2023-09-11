import psutil


# for proc in psutil.process_iter(['pid', 'name', 'username']):
#    print(proc.info)

def proc():
    processes = psutil.process_iter()
    data = []
    for process in processes:
        process_info = process.as_dict(attrs=['pid', 'name', 'status','memory_percent'])
        data.append(process_info)
    return data

