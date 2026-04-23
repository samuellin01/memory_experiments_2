import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('Italy. October 1, 2022,'), shell=True, check=True)
import time; time.sleep(0.05)