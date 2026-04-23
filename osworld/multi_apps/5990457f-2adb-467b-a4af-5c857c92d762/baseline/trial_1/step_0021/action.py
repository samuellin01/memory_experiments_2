import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cat /tmp/lecun_scholar.html | head -20\n'), shell=True, check=True)
import time; time.sleep(0.05)