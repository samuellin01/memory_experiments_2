import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('unzip ~/Downloads/happy-extension-v0-0-1.zip -d ~/'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('Projects/\n'), shell=True, check=True)
import time; time.sleep(0.05)