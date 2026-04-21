import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('https://www.aclweb.org/portal/acl-best-paper-award'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('s\n'), shell=True, check=True)
import time; time.sleep(0.05)