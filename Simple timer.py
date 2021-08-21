import time, keyboard

def Timer(delay, secs):
    time.sleep(5)
    for i in range(secs, 0, -1):
        time.sleep(delay)
        keyboard.write(f"{i}")
        keyboard.press("enter")
        print(delay*1000)

timer = int(input("Timer: "))
delay = int(input("Delay in s: "))
Timer(delay, timer)


