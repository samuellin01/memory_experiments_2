import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('mkdir -p ~/Test/Speed\n'), shell=True, check=True)
import time; time.sleep(0.05)