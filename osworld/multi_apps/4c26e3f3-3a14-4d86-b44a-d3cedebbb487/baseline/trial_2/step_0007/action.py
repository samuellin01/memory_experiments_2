import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('original_image.png'), shell=True, check=True)
import time; time.sleep(0.05)