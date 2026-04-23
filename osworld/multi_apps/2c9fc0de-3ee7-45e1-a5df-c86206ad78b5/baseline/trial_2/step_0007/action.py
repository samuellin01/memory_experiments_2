import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('find . -maxdepth 2 -name ".git" -type d 2>/dev/nul'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('l\n'), shell=True, check=True)
import time; time.sleep(0.05)