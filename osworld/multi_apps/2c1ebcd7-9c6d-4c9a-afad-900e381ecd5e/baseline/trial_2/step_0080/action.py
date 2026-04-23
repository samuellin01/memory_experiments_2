import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('for%20web.pdf'), shell=True, check=True)
import time; time.sleep(0.05)