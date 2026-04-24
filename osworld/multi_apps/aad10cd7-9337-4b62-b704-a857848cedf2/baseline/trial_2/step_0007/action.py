import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pip3 install python-docx beautifulsoup4 2>/dev/nul'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('l || pip install python-docx beautifulsoup4\n'), shell=True, check=True)
import time; time.sleep(0.05)