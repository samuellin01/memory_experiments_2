import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pip install openpyxl reportlab PyPDF2 pdfrw 2>/dev'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('/null | tail -5\n'), shell=True, check=True)
import time; time.sleep(0.05)