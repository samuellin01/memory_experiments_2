import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('df -h / && pip install -r /home/user/instructor-em'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('bedding/requirements.txt\n'), shell=True, check=True)
import time; time.sleep(0.05)