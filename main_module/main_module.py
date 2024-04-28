import os

from colors.colors                 import Colors
from system_info.system_info       import get_system_info
from window_manager.window_manager import get_window_manager

def main():
    hostname, os_info, kernel, uptime, packages, memory = get_system_info()
    os_name,  os_arch                                   = os_info.split(None, 1)
    env_type, window_manager                            = get_window_manager()

    print(f"""
{Colors.RBC}        /\\        {Colors.RBC}{os.getlogin()}{Colors.RBW}@{Colors.RBC}{hostname}{Colors.reset}
{Colors.RBC}       /^^\\       {Colors.RBC}OS:        {Colors.RBW}{os_name} {os_arch}{Colors.reset}
{Colors.RBC}      /\\   \\      {Colors.RBC}KERNEL:    {Colors.RBW}{kernel}{Colors.reset}
{Colors.RBC}     /  {Colors.RC}__  \\     {Colors.RBC}UPTIME:    {Colors.RBW}{uptime}{Colors.reset}
{Colors.RC}    /  (  )  \\    {Colors.RBC}PACKAGES:  {Colors.RBW}{packages}{Colors.reset}
{Colors.RC}   / __|  |__\\\\   {Colors.RBC}MEMORY:    {Colors.RBW}{memory}{Colors.reset}
{Colors.RC}  ///        \\\\\\  {Colors.RBC}{env_type}:        {Colors.RBW}{window_manager}{Colors.reset}
""")
