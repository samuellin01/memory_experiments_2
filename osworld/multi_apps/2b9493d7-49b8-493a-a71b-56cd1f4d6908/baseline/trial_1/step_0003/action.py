import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('kill -9 1951\n'), shell=True, check=True)
import time; time.sleep(0.05)