import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote("pdftk ~/Desktop/book/'Spectral Graph Theory.pdf' d"), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote("ump_data | grep -A2 'BookmarkTitle'\n"), shell=True, check=True)
import time; time.sleep(0.05)