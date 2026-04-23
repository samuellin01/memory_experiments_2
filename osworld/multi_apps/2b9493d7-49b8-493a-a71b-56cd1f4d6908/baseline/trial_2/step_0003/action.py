import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('kill -9 2019\n'), shell=True, check=True)
import time; time.sleep(0.05)