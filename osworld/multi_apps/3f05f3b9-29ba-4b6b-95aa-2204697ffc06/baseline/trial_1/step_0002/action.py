import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('which kid3-cli\n'), shell=True, check=True)
import time; time.sleep(0.05)