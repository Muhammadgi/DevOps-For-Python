import psutil



def check_cpu():

    cpu_percent=psutil.cpu_percent(interval=1)
    if cpu_percent > 80:
        print("Email Sent")
    else:
        print(f"The Cpu in Safe Mode {cpu_percent} Enjoy")

def check_boot_time():
    boot_time=psutil.boot_time()
    print(boot_time)

def check_mem():
    mem_per=psutil.virtual_memory()    
    print(mem_per)

def master_function():
    check_cpu()
    check_mem()
    check_boot_time()


master_function()