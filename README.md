# zju-dailyhealth-autocheck
利用python schedule库实现定时自动健康打卡

Mrli学长原库链接：https://github.com/Freedomisgood/When_Coding_in_ZJU/tree/main/Health_Checkin

登录接口地代码fork自Mrli学长，其中改动有：

1. 将地理位置判断取消，直接使用确定地点地编码
2. 可以采用jenkins部署任务，实现定时，周期性，自动执行打卡任务
3. 可以使用windows cmd或shell窗口，执行脚本，实现定时和周期性地打卡
4. jenkins部署任务时，可以采用job进行添加账户密码

使用说明：

1. Daka.py为打卡脚本，其原理为从同文件夹下的account.json文件（需要自己在本地新建）中读取用户数据,用户数据格式如下,其中account和password对应的统一认证的账号密码

```JSON
[
    {
        "account": "123123123",
        "password": "xxxxx"
    },
    {
        "account": "123123123",
        "password": "xxxx"
    }
]
```

2. schedule_task为定时脚本，可以设置每日固定时间或者固定每隔一个周期时间进行一次打卡操作
3. add_account为加账户脚本，用户可执行`python -u .\add_account.py 123123123 xxxx`给account.json文件增加账号密码信息，此功能为jenkins部署时使用，正常直接修改account.json文件即可
4. Jenkins:一个可以将自己计算机作为服务器，定时或者用某些条件触发的情况下自动跑自己想要的脚本的开源自动化服务器。jenkins说明请参考https://www.jenkins.io

## 注意
请勿将本地的account.json文件push到github库，里面可能含有本人的信息，可能会造成信息泄漏！！
## 声明

本项目为Python学习交流的开源非营利项目，仅作为程序员之间相互学习交流之用。

严禁用于商业用途，禁止使用本项目进行任何盈利活动。

使用者请遵从相关政策。对一切非法使用所产生的后果，我们概不负责。

本项目对您如有困扰请联系我们删除。
