# 哈深研究生成绩推送
<p align='right'>第一时间用邮件通知你新出的考试成绩</p>

1.在 config.py 中填入正确信息

2.```$ python3 run.py``` 

3.后台运行  ```$ nohup python3 run.py > logfile 2>&1 &```

4.为了避免个人信息暴露，可以把代码编译成.pyc后再使用

``````bash
$ python3 -m compileall run.py message.py spider.py config.py -b
$ python3 run.pyc
``````

