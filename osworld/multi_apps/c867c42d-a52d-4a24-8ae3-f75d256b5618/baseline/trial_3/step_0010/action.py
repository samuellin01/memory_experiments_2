import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('libreoffice --headless --calc --convert-to xlsx ~/'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('Desktop/contacts.csv --outdir ~/Desktop/\n'), shell=True, check=True)
import time; time.sleep(0.05)