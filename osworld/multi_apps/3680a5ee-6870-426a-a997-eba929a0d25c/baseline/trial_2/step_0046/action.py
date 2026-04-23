import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('killall soffice.bin 2>/dev/null; sleep 2; soffice '), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('--calc ~/Desktop/output.csv\n'), shell=True, check=True)
import time; time.sleep(0.05)