import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('find /home/user -maxdepth 3 -type d -name "OSWorld'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('" 2>/dev/null\n'), shell=True, check=True)
import time; time.sleep(0.05)