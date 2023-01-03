import sys
import time
import win32api

forever = True
handled_ctrl_type = None

def handler(ctrl_type):
    global forever, handled_ctrl_type
    forever = False
    handled_ctrl_type = ctrl_type
    print("HANDLER")
    return True

def main(args = None):
    win32api.SetConsoleCtrlHandler(handler, True)
    n = 0
    while forever:
        time.sleep(1)
        print(n)
        n = n + 1
    print("exiting...", handled_ctrl_type)
    return 0

if __name__ == '__main__':
    sys.exit(main())