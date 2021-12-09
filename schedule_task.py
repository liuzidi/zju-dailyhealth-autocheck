import schedule
import time
from check import Daka



if __name__ == "__main__":
    # 定时任务1:每6个小时打一次卡
    schedule.every(6).hours.do(Daka)
    # 定时任务2:每天凌晨00：01时间打卡
    schedule.every().day.at("00:01").do(Daka)
    print("启动打卡系统")
    Daka()
    print("6小时后或者明天凌晨打卡....")
    while True:
        schedule.run_pending()
        time.sleep(10)