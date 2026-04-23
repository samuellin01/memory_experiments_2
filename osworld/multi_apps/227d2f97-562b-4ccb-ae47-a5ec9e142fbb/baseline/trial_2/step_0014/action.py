import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('rm ~/Desktop/temp_image.png ~/Desktop/input.xcf\n'), shell=True, check=True)
import time; time.sleep(0.05)