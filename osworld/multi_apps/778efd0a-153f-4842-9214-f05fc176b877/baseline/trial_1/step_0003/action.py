import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ffmpeg -i /home/user/Desktop/planet.mp4 -vn -acode'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('c pcm_s16le /home/user/Desktop/planet.wav\n'), shell=True, check=True)
import time; time.sleep(0.05)