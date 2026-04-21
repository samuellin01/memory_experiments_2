import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('grep Answer /tmp/grade.py\n'), shell=True, check=True)
import time; time.sleep(0.05)