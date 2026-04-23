import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('file ~/Desktop/DOC_248090371271806684.pdf && ls -l'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('a ~/Desktop/DOC_248090371271806684.pdf\n'), shell=True, check=True)
import time; time.sleep(0.05)