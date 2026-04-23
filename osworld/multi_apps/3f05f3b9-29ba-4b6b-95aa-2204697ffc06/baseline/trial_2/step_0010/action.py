import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('for f in *.mp3; do echo "=== $f ==="; id3v2 -l "$f'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('" | grep -E "TPE1|TIT2"; done\n'), shell=True, check=True)
import time; time.sleep(0.05)