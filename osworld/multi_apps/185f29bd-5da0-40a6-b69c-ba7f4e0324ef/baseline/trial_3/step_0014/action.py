import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cat /tmp/pdf_fields.txt | head -60\n'), shell=True, check=True)
import time; time.sleep(0.05)