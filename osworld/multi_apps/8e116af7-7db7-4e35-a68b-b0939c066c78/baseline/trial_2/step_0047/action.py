import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cat /tmp/r3.txt\n'), shell=True, check=True)
import time; time.sleep(0.05)