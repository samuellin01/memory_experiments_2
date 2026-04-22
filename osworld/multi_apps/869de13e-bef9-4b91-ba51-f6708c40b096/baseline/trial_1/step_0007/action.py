import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pdftotext ~/Desktop/DOC_2480903712718068684.pdf - '), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('2>/dev/null | head -20\n'), shell=True, check=True)
import time; time.sleep(0.05)