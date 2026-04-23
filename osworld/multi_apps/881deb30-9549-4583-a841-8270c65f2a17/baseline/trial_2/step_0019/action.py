import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pip install tabula-py camelot-py[cv] 2>/dev/null |'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote(' tail -5\n'), shell=True, check=True)
import time; time.sleep(0.05)