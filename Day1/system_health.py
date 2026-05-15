import psutil

def check_sys_metrics(cpu_threshold,mem_threshold):

    cpu_metrics=psutil.cpu_percent(interval=1)

    if cpu_metrics >=cpu_threshold:

        print("Cpu is in Danger Mode")
    else:
        print(f"The Cpu in safe mode with usage of {cpu_metrics}")
        
    mem_metrics=psutil.virtual_memory()

    if mem_metrics.percent >= mem_threshold:

        print("The Memory is out of usage")
    else:
        print(f"The Memory is in safe mode with usage of {mem_metrics}")

    disk_metrics=psutil.disk_partitions()
    print(disk_metrics)

cpu_threshold=int(input("Enter cpu threshold"))
mem_threshold=int(input("Enter mem threshold"))
result=check_sys_metrics(cpu_threshold,mem_threshold)
print(result)
