import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('eog ~/Desktop/receipt_0.jpeg &\n'), shell=True, check=True)
import time; time.sleep(0.05)