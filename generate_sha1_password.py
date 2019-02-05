import sys
from notebook.auth import passwd
print(passwd(sys.stdin.readline().strip()))
