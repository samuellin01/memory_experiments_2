import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote("grep -c 'script' /tmp/imdb_top.html\n"), shell=True, check=True)
import time; time.sleep(0.05)