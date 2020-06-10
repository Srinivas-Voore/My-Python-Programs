import time
from plyer import notification

if __name__=='__main__':
    while True:
        notification.notify(
        title='study smart',
        message='use all resources available',
        app_icon=r"C:\Users\srinivas\Desktop\dn1\bulb.ico",
        timeout=10
        )
        time.sleep(60*60)
