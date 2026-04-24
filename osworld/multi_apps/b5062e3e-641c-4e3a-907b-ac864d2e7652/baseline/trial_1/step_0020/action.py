import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pdftotext -f 1 -l 2 ~/Documents/Papers/niu_screena'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('gent.pdf - | grep -B2 -A2 "@"\n'), shell=True, check=True)
import time; time.sleep(0.05)