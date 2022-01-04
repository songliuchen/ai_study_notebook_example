"""
彩云在线翻译
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyperclip
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
import os
import logging

def init(driver_path):
	s = Service(driver_path)
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('window-size=1920x1080')
	chrome_options.add_argument('blink-settings=imagesEnabled=false')
	driver = webdriver.Chrome(service=s)
	return driver

def paste_it(text,driver,is_windows,trans_time = 3):
	input_id = 'textarea'
	input_area = driver.find_element(by=By.ID,value=input_id)
	pyperclip.copy(text)
	input_area.clear()

	if is_windows:
		input_area.send_keys(Keys.CONTROL + "v")
	else:
		input_area.send_keys(Keys.COMMAND+ "v")
	time.sleep(trans_time)
	button_css = '//button[@node-type="target-copy-btn"]'
	button = driver.find_element(by=By.XPATH,value=button_css)
	y = button.location['y']
	driver.execute_script("window.scrollTo(0, {})".format(y - 150))
	time.sleep(2)

	button.click()
	time.sleep(1)
	content = pyperclip.paste()
	input_area.clear()
	pyperclip.copy('')
	return content

def tranlate(driver,file_name,is_windows,is_en=True,trans_time = 3):
	# 翻译地址(自动检测语言）
	url = 'https://fanyi.caiyunapp.com/#/'
	source_name = ".json"
	target_name = "_caiyun_en.json"
	if not is_en:
		file_name = file_name.replace(source_name,target_name)
		source_name = target_name
		target_name = "_caiyun.json"

	driver.get(url)
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
					#已经翻译过的的记录跳过
					if item["id"] in logs:
						continue
					print("第 %s 条,%s-----%s" % (len(logs) + 1, item["id"], item["text"]))
					trans_text = paste_it(item["text"], driver, is_windows, trans_time)
					if trans_text is not None and len(trans_text) > 0 and trans_text != before_trans and trans_text != item["text"]:
						# 翻译一条，保存一条，避免异常丢失数据
						item_copy = item.copy()
						item_copy["text"] = trans_text
						before_trans = trans_text
						# 已翻译，添加到已翻译集合
						logs.append(item["id"])
						target_f.write(json.dumps(item_copy, ensure_ascii=False) + "\n")
						target_f.flush()
				else:
					done_source = 1


def execute(is_windows,is_en,file_path,trans_time):
	"""
	@param is_windows 是否windows系统
	@param is_en 是否翻译成英文
	@param file_path 文件路径
	@param trans_time 单个文本翻译时长，根据翻译文本长度自行调整
	"""
	if is_windows:
		driver_path = "plugin/chromedriver.exe"
	else:
		driver_path = "plugin/chromedriver"
	driver = init(driver_path)
	try:
		tranlate(driver,file_path,is_windows,is_en,trans_time)
		print("翻译完成。。。。。")
	except Exception as e:
		logging.exception(e)
		print("超出使用次数限制，正在重启。。。。")
		driver.quit()
		execute(is_windows, is_en, file_path, 3)


if __name__ == '__main__':
	#先将所有问题都翻译成英文
	execute(False,True,"data/sample_data.json",3)
	#再将英文翻译回正文
	execute(False, False, "data/sample_data.json", 3)