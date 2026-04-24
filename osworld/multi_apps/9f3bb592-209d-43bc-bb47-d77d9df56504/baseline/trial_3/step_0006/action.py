import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ffmpeg -i /home/user/video.mp4 -map 0:v -map 0:a -'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('c copy /home/user/video_nosub.mp4\n'), shell=True, check=True)
import time; time.sleep(0.05)