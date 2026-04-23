import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('kill %1 2>/dev/null; killall gimp 2>/dev/null\n'), shell=True, check=True)
import time; time.sleep(0.05)