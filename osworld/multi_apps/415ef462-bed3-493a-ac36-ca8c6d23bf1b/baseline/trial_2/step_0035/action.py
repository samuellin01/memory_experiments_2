import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('AWS\t2023.12\t10.02\n'), shell=True, check=True)
import time; time.sleep(0.05)