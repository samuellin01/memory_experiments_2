import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pdftotext ecs15.pdf - | head -200\n'), shell=True, check=True)
import time; time.sleep(0.05)