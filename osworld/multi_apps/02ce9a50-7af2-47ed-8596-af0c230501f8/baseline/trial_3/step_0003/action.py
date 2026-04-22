import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('gnome-screenshot -w -f ~/Desktop/ls.png\n'), shell=True, check=True)
import time; time.sleep(0.05)