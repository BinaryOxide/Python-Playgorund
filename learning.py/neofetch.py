import platform
import psutil
import socket
import datetime
import GPUtil

# ANSI true color codes
RED = "\033[38;2;255;131;131m" 
BLUE = "\033[38;2;2;232;174m"     # #02e8ae
YELLOW = "\033[38;2;172;174;175m" # #acaeaf
RESET = "\033[0m"

def python_neofetch():
    # System Info
    system = platform.system()
    node = platform.node()
    release = platform.release()
    arch = platform.machine()
    processor = platform.processor()

    # CPU/RAM
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    cpu_usage = f"{psutil.cpu_percent(interval=1)}%"
    ram = psutil.virtual_memory()
    ram_used = f"{round(ram.used / (1024**3), 1)}GB"
    ram_total = f"{round(ram.total / (1024**3), 1)}GB"

    # Disk
    disk = psutil.disk_usage('/')
    disk_used = f"{round(disk.used / (1024**3), 1)}GB"
    disk_total = f"{round(disk.total / (1024**3), 1)}GB"

    # Network
    host_ip = socket.gethostbyname(socket.gethostname())
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time

    # GPU
    gpus = GPUtil.getGPUs()
    gpu_info = f"{gpus[0].name} ({gpus[0].memoryUsed}MB / {gpus[0].memoryTotal}MB)" if gpus else "No GPU detected"

    # Output
    print(f"""
{RED}
{RED}  llllllllllll  llllllllllll {BLUE} OS: {RESET}{system} {release}
{RED}  llllllllllll  llllllllllll {BLUE} Host: {RESET}{node} ({host_ip})
{RED}  llllllllllll  llllllllllll {BLUE} Kernel: {RESET}{release}
{RED}  llllllllllll  llllllllllll {BLUE} Uptime: {RESET}{str(uptime).split('.')[0]}
{RED}  llllllllllll  llllllllllll {BLUE} Arch: {RESET}{arch}
{RED}  llllllllllll  llllllllllll {BLUE} CPU: {RESET}{processor}
{RED}                             {BLUE} Cores: {RESET}{cpu_cores} (Threads: {cpu_threads})
{RED}  llllllllllll  llllllllllll {BLUE} CPU Usage: {YELLOW}{cpu_usage}{RESET}
{RED}  llllllllllll  llllllllllll {BLUE} RAM: {YELLOW}{ram_used} / {ram_total}{RESET}
{RED}  llllllllllll  llllllllllll {BLUE} Disk: {YELLOW}{disk_used} / {disk_total}{RESET}
{RED}  llllllllllll  llllllllllll {BLUE} GPU: {RESET}{gpu_info}
{RED}  llllllllllll  llllllllllll {BLUE} Date: {RESET}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{RED}  llllllllllll  llllllllllll  <\\>--------------------------------<\\>
{RED}  
{RESET}
""")

if __name__ == "__main__":
    python_neofetch()
