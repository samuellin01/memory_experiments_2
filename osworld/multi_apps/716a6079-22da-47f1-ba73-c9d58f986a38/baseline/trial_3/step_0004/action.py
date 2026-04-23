import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('xclip -selection clipboard -o\n'), shell=True, check=True)
import time; time.sleep(0.05)