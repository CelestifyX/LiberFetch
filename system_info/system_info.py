from functions.functions import *

def get_system_info():
    hostname   = subprocess.check_output(['hostnamectl', '--transient'], text=True).strip()
    os_info    = subprocess.check_output(['cat', '/etc/os-release'],  text=True).splitlines()
    os_name    = ''
    os_version = ''

    for line in os_info:
        if line.startswith('NAME='):
            os_name    = line.split('=')[1].strip('"')
        elif line.startswith('VERSION='):
            os_version = line.split('=')[1].strip('"')

    os_arch     = os.uname().machine
    kernel      = subprocess.check_output(['uname',  '-sr'], text=True).strip()
    uptime      = subprocess.check_output(['uptime', '-p'],  text=True).strip().split('up ')[-1]
    memory_info = subprocess.check_output(['free',   '-m'],  text=True).splitlines()[1]

    packages    = list_packages()
    memory      = get_info_memory(memory_info)

    return hostname, f"{os_name} {os_version}{os_arch}", kernel, uptime, packages, memory
