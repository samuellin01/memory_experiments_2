import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cat ~/.config/google-chrome/Default/Preferences | '), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('python3 -m json.tool | grep -i proxy\n'), shell=True, check=True)
import time; time.sleep(0.05)