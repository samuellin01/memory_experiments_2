import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('The Lost Symbol Dan Brown'), shell=True, check=True)
import time; time.sleep(0.05)