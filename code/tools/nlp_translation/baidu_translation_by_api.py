"""
百度api 在线翻译
"""
import json
import requests
import random
import time
from hashlib import md5
import os
import logging

def paste_it(text,is_en):
    try:
        # 通过https://api.fanyi.baidu.com/创建对应的应用即可获取
        appid = '你的app_id'
        appkey = '你的app key'
        endpoint = 'http://api.fanyi.baidu.com'
        path = '/api/trans/vip/translate'
        url = endpoint + path

        def make_md5(s, encoding='utf-8'):
            return md5(s.encode(encoding)).hexdigest()

        salt = random.randint(32768, 65536)
        sign = make_md5(appid + text + str(salt) + appkey)
        #免费版1秒内只能请求一次
        time.sleep(1)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        if is_en:
            from_lang = "zh"
            to_lang = "en"
        else:
            from_lang = "en"
            to_lang = "zh"
        payload = {'appid': appid, 'q': text, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
        r = requests.post(url, params=payload, headers=headers)
        result = r.json()
        if "trans_result" in result:
            dsts = []
            for result_dist in result["trans_result"]:
                dsts.append(result_dist["dst"])
            dst = '\n'.join(dsts)
            return dst
        else:
            return ""
    except:
        return ""

def tranlate(file_name,is_en=True):
    # 翻译地址(自动检测语言）
    source_name = ".json"
    target_name = "_baidu_en.json"
    if not is_en:
        file_name = file_name.replace(source_name, target_name)
        source_name = target_name
        target_name = "_baidu.json"

    trans_file = file_name.replace(source_name, target_name)
    mode1 = 'r'
    mode2 = "a+"
    if not os.path.exists(trans_file):
        mode1 = 'w+'
        mode2 = 'w+'
    # 获取已经翻译过的记录ID
    with open(trans_file, mode=mode1, encoding='utf-8') as log_f:
        logs = []
        if log_f.readable():
            done = 0
            while not done:
                item = log_f.readline()
                if item != '':
                    if len(item) < 2:
                        continue
                    if item.endswith("\n"):
                        item = item[0:-1]
                    logs.append(json.loads(item)["id"])
                else:
                    done = 1
    before_trans = ""
    with open(trans_file, encoding='utf-8', mode=mode2) as target_f:
        with open(file_name, 'r', encoding='utf-8') as source_f:
            done_source = 0
            while not done_source:
                item_source = source_f.readline()
                if item_source != '':
                    if item_source.endswith("\n"):
                        item_source = item_source[0:-1]
                    if len(item_source) < 2:
                        continue
                    item = json.loads(item_source)
                    # 已经翻译过的的记录跳过
                    if item["id"] in logs:
                        continue
                    print("第 %s 条,%s-----%s" % (len(logs) + 1, item["id"], item["text"]))
                    trans_text = paste_it(item["text"],is_en)
                    if trans_text is not None and len(trans_text) > 0 and trans_text != before_trans and trans_text != \
                            item["text"]:
                        # 翻译一条，保存一条，避免异常丢失数据
                        item_copy = item.copy()
                        item_copy["text"] = trans_text
                        before_trans = trans_text
                        # 已翻译，添加到已翻译集合
                        logs.append(item["id"])
                        target_f.write(json.dumps(item_copy, ensure_ascii=False) + "\n")
                        target_f.flush()
                    else:
                        print(item["text"]+"翻译异常")
                else:
                    done_source = 1

def execute(is_en,file_path):
    """
    	@param is_en 是否翻译成英文
    	@param file_path 文件路径
    	"""
    try:
        tranlate(file_path, is_en)
        print("翻译完成。。。。。")
    except Exception as e:
        logging.exception(e)
        execute(is_en, file_path)


if __name__ == '__main__':
    # 先将所有问题都翻译成英文
    execute(True, "data/sample_data.json")
    # 再将英文翻译回正文
    execute(False, "data/sample_data.json")