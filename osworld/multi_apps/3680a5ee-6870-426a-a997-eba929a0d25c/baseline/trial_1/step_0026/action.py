import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('xdotool search --name "output.csv" windowactivate '), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('--sync windowfocus --sync windowraise\n'), shell=True, check=True)
import time; time.sleep(0.05)