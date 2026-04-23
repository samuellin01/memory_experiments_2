import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('00H:00m:08s'), shell=True, check=True)
import time; time.sleep(0.05)