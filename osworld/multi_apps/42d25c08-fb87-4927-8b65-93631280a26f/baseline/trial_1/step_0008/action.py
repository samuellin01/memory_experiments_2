import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('sudo apt-get install -y libpcre3-dev\n'), shell=True, check=True)
import time; time.sleep(0.05)