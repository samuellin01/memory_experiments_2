import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('which sar || sudo apt-get install -y sysstat\n'), shell=True, check=True)
import time; time.sleep(0.05)