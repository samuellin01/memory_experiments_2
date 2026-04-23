import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('Lec 2 (12:00-14:00)'), shell=True, check=True)
import time; time.sleep(0.05)