import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('xdotool windowactivate 23290748 && xdotool windowf'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ocus 23290748 && xdotool windowraise 23290748\n'), shell=True, check=True)
import time; time.sleep(0.05)