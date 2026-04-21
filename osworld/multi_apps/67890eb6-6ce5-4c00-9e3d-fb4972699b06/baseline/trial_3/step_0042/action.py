import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('https://acl2020.org/blog/ACL-2020-best-papers/\n'), shell=True, check=True)
import time; time.sleep(0.05)