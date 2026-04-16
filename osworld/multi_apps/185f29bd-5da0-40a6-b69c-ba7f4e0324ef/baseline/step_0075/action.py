import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('xdg-open "/home/user/Desktop/Emily Johnson.pdf" &\n'), shell=True, check=True)
import time; time.sleep(0.05)