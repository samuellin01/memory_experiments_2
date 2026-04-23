import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('2023.12\t'), shell=True, check=True)
import time; time.sleep(0.05)