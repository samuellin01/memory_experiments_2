import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cd ~/Desktop && ls -la receipt*\n'), shell=True, check=True)
import time; time.sleep(0.05)