import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ICML 2019 location city'), shell=True, check=True)
import time; time.sleep(0.05)