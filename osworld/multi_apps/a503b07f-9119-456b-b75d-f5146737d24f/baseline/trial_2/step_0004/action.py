import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('sudo apt install -y imagemagick-6.q16\n'), shell=True, check=True)
import time; time.sleep(0.05)