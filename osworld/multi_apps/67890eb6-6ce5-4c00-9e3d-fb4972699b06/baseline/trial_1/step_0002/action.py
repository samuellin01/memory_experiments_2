import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('https://aclanthology.org/volumes/2022.acl-long/\n'), shell=True, check=True)
import time; time.sleep(0.05)