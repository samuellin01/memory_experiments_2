import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('wmctrl -a output.csv 2>/dev/null || xdotool search'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote(' --name "output" windowactivate windowraise\n'), shell=True, check=True)
import time; time.sleep(0.05)