import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('which id3v2 mid3v2 kid3-cli 2>/dev/null; dpkg -l |'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote(' grep -E "id3v2|mutagen|kid3" 2>/dev/null\n'), shell=True, check=True)
import time; time.sleep(0.05)