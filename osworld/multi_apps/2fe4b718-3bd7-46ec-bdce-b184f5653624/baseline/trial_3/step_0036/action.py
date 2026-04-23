import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('dpkg -l | grep gimp-python 2>/dev/null; apt list -'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('-installed 2>/dev/null | grep gimp\n'), shell=True, check=True)
import time; time.sleep(0.05)