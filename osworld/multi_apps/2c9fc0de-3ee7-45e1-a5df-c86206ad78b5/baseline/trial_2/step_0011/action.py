import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('git add -A && git commit -m "daily update" && git '), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('push origin main\n'), shell=True, check=True)
import time; time.sleep(0.05)