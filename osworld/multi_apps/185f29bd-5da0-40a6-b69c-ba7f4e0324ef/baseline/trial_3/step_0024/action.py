import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cat /tmp/pdf_fields.txt | nl\n'), shell=True, check=True)
import time; time.sleep(0.05)