import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('eog ~/Pictures/picture1.jpg &\n'), shell=True, check=True)
import time; time.sleep(0.05)