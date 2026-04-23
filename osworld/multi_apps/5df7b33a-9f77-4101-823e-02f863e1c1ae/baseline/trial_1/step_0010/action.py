import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote("pdftotext ~/Desktop/book/'Spectral Graph Theory.pd"), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('f\' - | grep -n "^[0-9] "\n'), shell=True, check=True)
import time; time.sleep(0.05)