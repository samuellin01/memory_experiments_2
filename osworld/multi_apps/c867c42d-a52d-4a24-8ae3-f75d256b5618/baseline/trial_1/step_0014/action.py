import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cd ~/Desktop && libreoffice --calc --headless --co'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('nvert-to xlsx contacts.csv\n'), shell=True, check=True)
import time; time.sleep(0.05)