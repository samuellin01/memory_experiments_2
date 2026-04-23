import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('https://doi.org/10.1596/978-1-4648-0671-1'), shell=True, check=True)
import time; time.sleep(0.05)