import os
import subprocess

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

            if manager == "pacman":
                command.append("-Q")
            elif manager == "yay":
                command.append("-Q")
            elif manager == "snap":
                command.append("list")
            elif manager == "flatpak":
                command.extend(["list", "--columns=application"])

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
