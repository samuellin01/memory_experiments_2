import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote("wc -c /tmp/imdb_top.html && grep -o '<title>[^<]*<"), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote("/title>' /tmp/imdb_top.html\n"), shell=True, check=True)
import time; time.sleep(0.05)