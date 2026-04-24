import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('xdg-mime query default video/mp4\n'), shell=True, check=True)
import time; time.sleep(0.05)