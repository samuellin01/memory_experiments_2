import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('70'), shell=True, check=True)
import time; time.sleep(0.05)