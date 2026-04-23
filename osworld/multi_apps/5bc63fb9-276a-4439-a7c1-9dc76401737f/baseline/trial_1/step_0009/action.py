import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pip install python-docx 2>/dev/null | tail -1\n'), shell=True, check=True)
import time; time.sleep(0.05)