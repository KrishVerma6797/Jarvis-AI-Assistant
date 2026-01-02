import wmi
import psutil
import platform
import getpass
import os
from prettytable import PrettyTable
from speak import speak

def get_system_info():
    return {
        "OS": f"{platform.system()} {platform.release()} ({platform.version()})",
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "CPU Cores": os.cpu_count(),
        "Logical CPUs": psutil.cpu_count(logical=True),
        "RAM": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB",
        "Architecture": platform.architecture()[0],
        "User": getpass.getuser()
    }

def get_hardware_info():
    c = wmi.WMI()

    gpu = c.Win32_VideoController()[0].Name if c.Win32_VideoController() else "Unknown"
    battery = c.Win32_Battery()[0].EstimatedChargeRemaining if c.Win32_Battery() else "N/A"
    motherboard = c.Win32_BaseBoard()[0].Product if c.Win32_BaseBoard() else "Unknown"
    disk = c.Win32_DiskDrive()[0].Model if c.Win32_DiskDrive() else "Unknown"

    return {
        "GPU": gpu,
        "Battery": f"{battery}%" if battery != "N/A" else "Not Available",
        "Motherboard": motherboard,
        "Disk Drive": disk
    }

def tell_system_info():
    system = get_system_info()
    hardware = get_hardware_info()

    table = PrettyTable()
    table.field_names = ["Property", "Value"]

    for key, value in system.items():
        table.add_row([key, value])
        speak(f"{key} is {value}")

    for key, value in hardware.items():
        table.add_row([key, value])
        speak(f"{key} is {value}")

    print("\n🔧 Full System Information:\n")
    print(table)
