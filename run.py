import time
import spider
import message

scores_set = set()  # 记录已通知过的所有课程的课程号
def run():
    print('running...')
    while True:
        t = time.localtime()
        if t.tm_hour > 6 and t.tm_min % 10 == 0:  # 每天早上7点开始，每10分钟查一次
            scores = spider.get_score()  # 爬取成绩
            needs_inform = []  # 记录需要通知的课程
            for s in scores:
                if s[1] not in scores_set:
                    scores_set.add(s[1])
                    needs_inform.append((s[2], s[4]))

            if needs_inform:
                text = ''
                for i in needs_inform:  # 拼接消息
                    text += '%s: %s;\n' % (i)
                needs_inform = []  # 重置
                message.send(text)
            my_sleep(60)
        else:
            my_sleep(5)

def my_sleep(t):
    """防止sleep太长时间，进程被杀."""
    for i in range(t):
        time.sleep(i)

if __name__ == '__main__':
    run()
