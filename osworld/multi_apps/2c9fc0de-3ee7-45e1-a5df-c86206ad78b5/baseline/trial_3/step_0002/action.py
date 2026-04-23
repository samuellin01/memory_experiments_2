import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('git add . && git commit -m "daily update" && git p'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ush origin main\n'), shell=True, check=True)
import time; time.sleep(0.05)