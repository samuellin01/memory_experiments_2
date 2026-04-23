import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('aws-invoice-2312.pdf'), shell=True, check=True)
import time; time.sleep(0.05)