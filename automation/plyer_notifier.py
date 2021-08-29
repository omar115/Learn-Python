from plyer import notification
import time

while True:
    notification.notify(
        title = "Reminder",
        message = "Please take a break",
        app_icon = r'C:\Users\Ferntech\Desktop\git_workspace\Learn-Python\automation\sample.ico',
        timeout = 10
    )
    time.sleep(5)
