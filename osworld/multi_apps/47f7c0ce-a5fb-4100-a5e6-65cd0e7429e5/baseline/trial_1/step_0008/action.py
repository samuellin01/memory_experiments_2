import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ps aux | grep -i impress\n'), shell=True, check=True)
import time; time.sleep(0.05)