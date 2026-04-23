import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('google-chrome --remote-debugging-port=1337 "https:'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('//scholar.google.com/scholar?q=Tianlin+Tim+Shi" &\n'), shell=True, check=True)
import time; time.sleep(0.05)