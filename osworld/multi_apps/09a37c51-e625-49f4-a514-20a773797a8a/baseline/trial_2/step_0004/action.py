import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pip3 list 2>/dev/null | grep -i -E "rembg|pillow|o'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pencv"\n'), shell=True, check=True)
import time; time.sleep(0.05)