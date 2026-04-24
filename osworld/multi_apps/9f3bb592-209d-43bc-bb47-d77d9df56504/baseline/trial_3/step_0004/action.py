import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ffprobe /home/user/video.mp4 2>&1 | grep -i stream'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('\n'), shell=True, check=True)
import time; time.sleep(0.05)