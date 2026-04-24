import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ls ~/Desktop/ ~/Documents/ ~/Downloads/ ~/ 2>/dev/'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('null\n'), shell=True, check=True)
import time; time.sleep(0.05)