import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('https://doi.org/10.17705/1CAIS.04611'), shell=True, check=True)
import time; time.sleep(0.05)