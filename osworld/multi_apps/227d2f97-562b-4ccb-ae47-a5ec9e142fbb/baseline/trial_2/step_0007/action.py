import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cp ~/Desktop/*.xcf ~/Desktop/input.xcf\n'), shell=True, check=True)
import time; time.sleep(0.05)