import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('mkdir ~/Desktop/problematic\n'), shell=True, check=True)
import time; time.sleep(0.05)