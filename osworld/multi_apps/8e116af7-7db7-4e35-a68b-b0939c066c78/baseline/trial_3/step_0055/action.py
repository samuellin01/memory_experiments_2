import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('head -60 /tmp/all_receipts.txt\n'), shell=True, check=True)
import time; time.sleep(0.05)