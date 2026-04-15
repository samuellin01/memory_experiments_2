import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('find /home -name "ConferenceCity.xlsx" 2>/dev/null'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('\n'), shell=True, check=True)
import time; time.sleep(0.05)