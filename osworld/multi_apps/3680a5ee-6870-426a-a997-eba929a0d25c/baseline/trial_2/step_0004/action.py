import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('libreoffice --headless --convert-to csv --outdir /'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('tmp ~/Desktop/file2.ods\n'), shell=True, check=True)
import time; time.sleep(0.05)