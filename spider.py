import re
import hashlib
import requests
import config

username = config.JW_USERNAME
password = config.JW_PASSWORD
home_url = 'http://219.223.252.46:9001/login.do'
login_url = 'http://219.223.252.46:9001/j_acegi_login.do'
socre_url = 'http://219.223.252.46:9001/cjgl.v_allcj_yjs.do'
cookies = {'JSESSIONID': None}


def login():
    print('正在登录...')
    md5_obj = hashlib.md5(password.encode())
    md5_pwd = md5_obj.hexdigest()  # 登录密码需md5加密
    home_page = requests.get(home_url)  # 访问登录页面，获取cookie
    cookies['JSESSIONID'] = home_page.cookies['JSESSIONID']

    payload = {
        'j_captcha_response': '',
        'j_username': username,
        'j_password': md5_pwd,
        'x': 22,
        'y': 10
    }
    login_resp = requests.get(login_url, params=payload, cookies=cookies)
    if 'URP研究生教务系统' in login_resp.text:
        return True
    else:
        print('登录失败')
        return False

def get_score():
    result = []
    r = requests.get(socre_url, cookies=cookies)
    if 'gridData' not in r.text:  # 未登陆
        s = login()  # 重新登陆，验证cookie
        if s:
            # 重新获取成绩页面
            r = requests.get(socre_url, cookies=cookies)
        else:
            return result

    text = re.sub(r'\s', '', r.text)   # 去除所有空白
    score_list_str = re.search(r'vargridData=(.*);</script><tablewidth', text)  # 提取成绩列表-list
    if score_list_str:
        score_list_str = score_list_str.group(1)
        result = eval(score_list_str)  # 把字符串中的list转为python的list对象
        return result
    else:
        print('提取成绩列表失败')
        return result
