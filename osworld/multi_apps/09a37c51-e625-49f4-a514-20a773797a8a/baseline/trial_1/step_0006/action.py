import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('which gimp 2>&1 && pip3 install rembg 2>&1 | tail '), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('-5\n'), shell=True, check=True)
import time; time.sleep(0.05)