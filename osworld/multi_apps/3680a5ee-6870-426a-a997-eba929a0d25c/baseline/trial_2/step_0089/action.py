import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('xdotool search --class "gnome-terminal" windowmini'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('mize 2>/dev/null\n'), shell=True, check=True)
import time; time.sleep(0.05)