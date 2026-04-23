import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('which kid3-cli id3v2 mid3v2 eyeD3 2>/dev/null; dpk'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('g -l | grep -i kid3 2>/dev/null\n'), shell=True, check=True)
import time; time.sleep(0.05)