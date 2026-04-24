import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote("grep -o 'application/json[^<]*' /tmp/searching.htm"), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('l | head -5\n'), shell=True, check=True)
import time; time.sleep(0.05)