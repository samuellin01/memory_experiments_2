import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('curl -s https://api.github.com/repos/liangjs333/4t'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('h-year-in-tsinghua-eng/contents/ | grep \'"name"\'\n'), shell=True, check=True)
import time; time.sleep(0.05)