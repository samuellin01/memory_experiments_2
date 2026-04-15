import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('https://aclanthology.org/events/acl-2022/\n'), shell=True, check=True)
import time; time.sleep(0.05)