import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('xdotool search --name "output" windowactivate --sy'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('nc windowfocus --sync windowraise\n'), shell=True, check=True)
import time; time.sleep(0.05)