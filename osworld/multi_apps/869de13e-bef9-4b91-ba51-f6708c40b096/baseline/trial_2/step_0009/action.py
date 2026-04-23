import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pdftotext ~/Desktop/paper01.pdf - 2>/dev/null | he'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ad -20\n'), shell=True, check=True)
import time; time.sleep(0.05)