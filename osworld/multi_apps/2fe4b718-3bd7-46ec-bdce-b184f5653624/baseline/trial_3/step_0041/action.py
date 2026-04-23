import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('gimp -i -b "$(cat /tmp/gifmaker2.scm)" 2>&1 &\n'), shell=True, check=True)
import time; time.sleep(0.05)