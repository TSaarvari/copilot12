import os
import platform
import subprocess

def get_system_uptime():
    system = platform.system()
    try:
        if system == "Windows":
            # Use 'net stats srv' and parse output for Windows
            output = subprocess.check_output("net stats srv", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    return f"System uptime (since): {line.split('since',1)[1].strip()}"
        elif system == "Linux":
            # Use /proc/uptime for Linux
            with open("/proc/uptime", "r") as f:
                uptime_seconds = float(f.readline().split()[0])
                hours = int(uptime_seconds // 3600)
                minutes = int((uptime_seconds % 3600) // 60)
                seconds = int(uptime_seconds % 60)
                return f"System uptime: {hours}h {minutes}m {seconds}s"
        elif system == "Darwin":
            # Use 'uptime' command for macOS
            output = subprocess.check_output("uptime", shell=True, text=True)
            return f"System uptime: {output.strip()}"
        else:
            return "Unsupported operating system."
    except Exception as e:
        return f"Error retrieving uptime: {e}"

if __name__ == "__main__":
    print(get_system_uptime())
