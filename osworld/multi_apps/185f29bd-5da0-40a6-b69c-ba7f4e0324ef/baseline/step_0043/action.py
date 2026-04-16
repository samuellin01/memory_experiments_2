import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pip install fillpdf 2>/dev/null | tail -3\n'), shell=True, check=True)
import time; time.sleep(0.05)