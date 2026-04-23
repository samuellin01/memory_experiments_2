import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('sudo apt-get install -y sysstat 2>/dev/null && sar'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote(' 1 30 > ~/Desktop/System_Resources_Report.txt\n'), shell=True, check=True)
import time; time.sleep(0.05)