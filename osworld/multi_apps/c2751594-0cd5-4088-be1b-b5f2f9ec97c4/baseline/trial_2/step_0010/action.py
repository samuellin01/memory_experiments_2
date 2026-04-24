import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('gsettings get org.gnome.desktop.background picture'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('-uri\n'), shell=True, check=True)
import time; time.sleep(0.05)