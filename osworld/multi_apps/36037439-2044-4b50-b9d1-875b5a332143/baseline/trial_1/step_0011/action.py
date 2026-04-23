import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('https://scholar.google.com/citations?view_op=searc'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('h_authors&mauthors=Tianlin+Shi&hl=en\n'), shell=True, check=True)
import time; time.sleep(0.05)