import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pip install python-docx 2>/dev/null; python3 -c "i'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('mport docx; print(\'OK\')"\n'), shell=True, check=True)
import time; time.sleep(0.05)