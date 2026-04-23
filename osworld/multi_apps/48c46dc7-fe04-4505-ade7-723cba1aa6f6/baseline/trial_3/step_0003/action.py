import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cd /home/user/Documents/Projects/OSWorld\n'), shell=True, check=True)
import time; time.sleep(0.05)