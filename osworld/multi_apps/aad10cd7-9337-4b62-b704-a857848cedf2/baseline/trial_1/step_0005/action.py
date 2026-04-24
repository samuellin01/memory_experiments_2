import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('curl -s https://developer.apple.com/design/human-i'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('nterface-guidelines/searching | head -50\n'), shell=True, check=True)
import time; time.sleep(0.05)