import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)  # 暂停一秒
        t -= 1

    print("时间到！")

# 用户设置专注时间（分钟）
focus_time = int(input("设定专注时间（分钟）: ")) * 60
countdown(focus_time)
