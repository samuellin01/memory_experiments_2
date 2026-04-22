import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('find /home/user -name "*.xlsx" -o -name "*.xls" 2>'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('/dev/null | head -5\n'), shell=True, check=True)
import time; time.sleep(0.05)