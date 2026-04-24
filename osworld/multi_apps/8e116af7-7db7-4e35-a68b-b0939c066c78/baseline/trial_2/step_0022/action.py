import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('tesseract receipt_0.jpeg stdout 2>/dev/null\n'), shell=True, check=True)
import time; time.sleep(0.05)