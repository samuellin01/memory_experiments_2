import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('sudo apt-get install -y sysstat && sar -u 1 30 > ~'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('/Desktop/System_Resources_Report.txt\n'), shell=True, check=True)
import time; time.sleep(0.05)