import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ffprobe ~/Desktop/src.mp4 2>&1 | grep fps\n'), shell=True, check=True)
import time; time.sleep(0.05)