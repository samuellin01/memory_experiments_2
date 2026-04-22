import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pip install tabula-py camelot-py[cv] pdfplumber 2>'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('/dev/null | tail -5\n'), shell=True, check=True)
import time; time.sleep(0.05)