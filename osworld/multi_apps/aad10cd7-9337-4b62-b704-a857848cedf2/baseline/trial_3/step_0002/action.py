import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('https://developer.apple.com/design/human-interface'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('-guidelines/searching\n'), shell=True, check=True)
import time; time.sleep(0.05)