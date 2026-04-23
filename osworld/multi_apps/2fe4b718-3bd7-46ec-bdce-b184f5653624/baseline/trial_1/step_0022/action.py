import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('gimp -i -b - < /tmp/make_gif.scm &\n'), shell=True, check=True)
import time; time.sleep(0.05)