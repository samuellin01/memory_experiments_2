import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('code ~/Desktop/resize-image.scm\n'), shell=True, check=True)
import time; time.sleep(0.05)