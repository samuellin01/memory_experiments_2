import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('wmctrl -l 2>/dev/null || echo "wmctrl not availabl'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('e"\n'), shell=True, check=True)
import time; time.sleep(0.05)