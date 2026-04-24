import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ffmpeg -i /home/user/video.mp4 -map 0:s:0 /home/us'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('er/subtitles.srt\n'), shell=True, check=True)
import time; time.sleep(0.05)