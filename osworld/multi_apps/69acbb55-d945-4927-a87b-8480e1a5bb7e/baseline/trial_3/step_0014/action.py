import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cd /home/user && git clone https://github.com/xlan'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('g-ai/instructor-embedding\n'), shell=True, check=True)
import time; time.sleep(0.05)