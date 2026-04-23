import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pdftotext ~/Desktop/DOC_248090371271806684.pdf - 2'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('>/dev/null | head -20\n'), shell=True, check=True)
import time; time.sleep(0.05)