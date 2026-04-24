import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('head -15 /tmp/r0.txt\n'), shell=True, check=True)
import time; time.sleep(0.05)