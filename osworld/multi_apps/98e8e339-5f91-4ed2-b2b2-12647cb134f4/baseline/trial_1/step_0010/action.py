import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('Default Paragraph Style'), shell=True, check=True)
import time; time.sleep(0.05)