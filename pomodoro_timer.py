import time  
import os  
  
def pomodoro_timer(duration=25):  
    """  
    一个简单的Pomodoro计时器，默认持续时间为25分钟。  
    """  
    print(f"开始一个{duration}分钟的专注时钟。")  
    for remaining in range(duration * 60, 0, -1):  
        mins, secs = divmod(remaining, 60)  
        timer = '{:02d}:{:02d}'.format(mins, secs)  
        print(timer, end="\r")  
        time.sleep(1)  
    print("时间到！休息一下。")  
    os.system('say "时间到，休息一下。"')  # 如果你在MacOS上，这将会使你的电脑说出“时间到，休息一下。”  
  
# 开始一个25分钟的专注时钟  
pomodoro_timer()
