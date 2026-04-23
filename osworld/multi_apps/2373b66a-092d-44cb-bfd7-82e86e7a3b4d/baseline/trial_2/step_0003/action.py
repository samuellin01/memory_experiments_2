import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('sar 1 30 > ~/Desktop/System_Resources_Report.txt\n'), shell=True, check=True)
import time; time.sleep(0.05)