import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('gsettings get org.gnome.system.proxy mode\n'), shell=True, check=True)
import time; time.sleep(0.05)