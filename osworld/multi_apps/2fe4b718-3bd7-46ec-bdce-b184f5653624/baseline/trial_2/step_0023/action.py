import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('kill $(pgrep -f "gimp -i") 2>/dev/null; sleep 2\n'), shell=True, check=True)
import time; time.sleep(0.05)