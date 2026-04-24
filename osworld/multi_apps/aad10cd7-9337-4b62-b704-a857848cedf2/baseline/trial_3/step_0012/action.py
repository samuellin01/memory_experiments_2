import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote("grep -i 'script.*src' /tmp/searching.html | head -"), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('10\n'), shell=True, check=True)
import time; time.sleep(0.05)