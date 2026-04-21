import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cat /tmp/grade3.py\n'), shell=True, check=True)
import time; time.sleep(0.05)