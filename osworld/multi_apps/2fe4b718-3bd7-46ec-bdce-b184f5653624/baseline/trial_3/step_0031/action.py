import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('kill %1 2>/dev/null; killall gimp 2>/dev/null; sle'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ep 2\n'), shell=True, check=True)
import time; time.sleep(0.05)