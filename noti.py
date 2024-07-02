import sched
import time

from plyer import notification

event_schedule = sched.scheduler(time.time, time.sleep)

def do_something():
    notification_title = 'Hello There!💧💦'
    notification_message = 'Please drink water🚰 to Hydrate your body👩🏼‍🦰! Sending you love💛.'

    try:

        notification.notify(title = notification_title, message = notification_message, app_icon = None, timeout = 10, toast = False)
        print('Notification sent successfully')
    except Exception as e:
        print(f'failed to send notification{e}')

    event_schedule.enter(3600, 1, do_something, ())

event_schedule.enter(0, 1, do_something, ())
event_schedule.run()