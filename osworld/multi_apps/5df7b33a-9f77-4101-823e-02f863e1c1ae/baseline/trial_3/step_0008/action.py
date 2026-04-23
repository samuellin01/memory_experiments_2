import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pip3 install PyPDF2 2>/dev/null && echo "installed'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('" || echo "failed"\n'), shell=True, check=True)
import time; time.sleep(0.05)