import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('find /home/user/.thunderbird -name "daily" -type f'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote(' 2>/dev/null\n'), shell=True, check=True)
import time; time.sleep(0.05)