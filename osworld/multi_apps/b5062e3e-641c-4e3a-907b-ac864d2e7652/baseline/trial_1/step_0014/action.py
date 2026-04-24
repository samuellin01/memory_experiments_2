import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pdftotext -f 1 -l 1 ~/Documents/Papers/koh_visualw'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ebarena.pdf - | head -50\n'), shell=True, check=True)
import time; time.sleep(0.05)