from plyer import notification
import time

while True:
    notification.notify(
        title = "Reminder",
        message = "Please take a break",
        timeout = 5
    )
    time.sleep(30)
