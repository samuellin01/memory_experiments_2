import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('killall soffice.bin 2>/dev/null; sleep 2; libreoff'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ice --calc ~/Desktop/my_bookkeeping.xlsx &\n'), shell=True, check=True)
import time; time.sleep(0.05)