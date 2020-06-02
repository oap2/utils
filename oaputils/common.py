import json
import random
import string
from datetime import datetime, date
import time


def get_ts() -> str:
    ts = time.time()
    st = datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
    return st


def gen_password(count=1):
    """ generate password """
    src = string.ascii_letters + string.digits
    src_special = "!@#$%^&*()_+-=[]{}|'"
    list_passwds = []
    for i in range(int(count)):
        list_passwd_all = random.sample(src, 8)  # 从字母和数字中随机取8位
        list_passwd_all.extend(random.sample(string.digits, 1))  # 让密码中一定包含数字
        list_passwd_all.extend(random.sample(string.ascii_lowercase, 1))  # 让密码中一定包含小写字母
        list_passwd_all.extend(random.sample(string.ascii_uppercase, 1))  # 让密码中一定包含大写字母
        list_passwd_all.extend(random.sample(src_special, 1))  # 让密码中一定包含特殊字符
        random.shuffle(list_passwd_all)  # 打乱列表顺序
        str_passwd = ''.join(list_passwd_all)  # 将列表转化为字符串
        if str_passwd not in list_passwds:  # 判断是否生成重复密码
            list_passwds.append(str_passwd)
    return '\n'.join(list_passwds)


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)
