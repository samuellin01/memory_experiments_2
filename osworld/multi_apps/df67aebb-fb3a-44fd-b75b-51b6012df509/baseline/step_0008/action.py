import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('google-chrome --remote-debugging-port=1337 "https:'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('//dblp.org/search?q=Attention+is+All+you+Need" &\n'), shell=True, check=True)
import time; time.sleep(0.05)