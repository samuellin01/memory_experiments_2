import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('xdg-open "/home/user/Desktop/John Doe.pdf" &\n'), shell=True, check=True)
import time; time.sleep(0.05)