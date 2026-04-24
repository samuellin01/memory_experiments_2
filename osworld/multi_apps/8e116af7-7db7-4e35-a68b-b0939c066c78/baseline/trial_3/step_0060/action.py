import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote("sed -n '87,101p' /tmp/all_receipts.txt\n"), shell=True, check=True)
import time; time.sleep(0.05)