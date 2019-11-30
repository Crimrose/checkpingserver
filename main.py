import winsound
import subprocess
import keyboard
#Can use multiple IP change to ["127.0.0.1", "52.15.103.126"]
iplist=["52.15.103.126","127.0.0.1"]
check=True
try:
    while check:
        for ip in iplist:
            p = subprocess.Popen('ping '+ip,stdout=subprocess.PIPE)
            # the stdout=subprocess.PIPE will hide the output of the ping command
            p.wait()
            if p.poll():
                print(ip+" is down")
                winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)
            else:
                print(ip+" is up")
        if keyboard.read_key() == "esc":
            print("You pressed ESC")
            break
            check=False
except KeyboardInterrupt:
    pass