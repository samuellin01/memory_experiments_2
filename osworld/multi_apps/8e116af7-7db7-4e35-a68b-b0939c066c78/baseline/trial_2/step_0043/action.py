import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('grep -i "total\\|subtotal\\|tax\\|balance\\|date\\|stor'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('e" /tmp/r0.txt\n'), shell=True, check=True)
import time; time.sleep(0.05)