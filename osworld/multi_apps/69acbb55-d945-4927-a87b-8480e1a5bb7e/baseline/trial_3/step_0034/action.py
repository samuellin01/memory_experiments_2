import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pip install --no-cache-dir -r /home/user/instructo'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('r-embedding/requirements.txt\n'), shell=True, check=True)
import time; time.sleep(0.05)