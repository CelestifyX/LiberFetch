import os
import subprocess

from colors.colors import Colors

def check_command_exists(command):
    try:
        subprocess.run(["which", command], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def list_packages():
    package_managers = {
        "pacman":  "Pacman",
        "snap":    "Snap",
        "flatpak": "Flatpak",
        "yay":     "AUR"
    }

    installed_packages = []

    for manager, name in package_managers.items():
        if check_command_exists(manager):
            command = [manager]

            command_map =  {
                "pacman":  ["-Qq"],
                "yay":     ["-Qm"],
                "snap":    ["list"],
                "flatpak": ["list", "--columns=application"]
            }

            if manager in command_map:
                command.extend(command_map[manager])

            try:
                output       = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                package_list = output.stdout.split('\n')
                count        = (len(package_list) - 1)

                if count > 0:
                    installed_packages.append((name, count))
            except subprocess.CalledProcessError:
                pass

    installed_packages.sort(key=lambda x: x[1], reverse=True)
    return ', '.join(f"{count} ({name})" for name, count in installed_packages)

def get_info_memory(memory_info):
    total_memory = int(memory_info.split()[1])
    used_memory  = int(memory_info.split()[2])
    percentage   = round(((used_memory / total_memory) * 100))
    color        = (Colors.green if percentage <= 50 else (Colors.orange if percentage <= 80 else Colors.red))

    return f"{used_memory}MiB / {total_memory}MiB ({color}{percentage}%{Colors.RBW})"
