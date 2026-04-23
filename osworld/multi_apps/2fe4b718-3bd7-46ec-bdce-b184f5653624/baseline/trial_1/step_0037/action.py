import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('killall gimp 2>/dev/null; sleep 2\n'), shell=True, check=True)
import time; time.sleep(0.05)