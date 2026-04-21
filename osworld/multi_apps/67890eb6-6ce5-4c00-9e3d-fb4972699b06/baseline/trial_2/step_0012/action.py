import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('https://2021.aclweb.org/program/best-papers/\n'), shell=True, check=True)
import time; time.sleep(0.05)