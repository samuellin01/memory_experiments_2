import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('http://anima-ai.org'), shell=True, check=True)
import time; time.sleep(0.05)