import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ls -la ~/Documents/Finance/receipts/\n'), shell=True, check=True)
import time; time.sleep(0.05)