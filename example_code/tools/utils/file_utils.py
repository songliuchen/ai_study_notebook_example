import json


def read_file(path,mode = None,to_json=False,custon_convert = None):
    """
    文本解析
    @param path: 文档路径
    @param mode: 打开模式
    @param to_json:是否转json
    @param custon_convert:自定义处理方法
    @return:集合
    """
    result = []
    with open(path) as f:
        is_done = 0
        while is_done !=1:
            item = f.readline()
            if len(item)>0:
                if item.endswith("\n"):
                    item = item[0:-1]
                if to_json:
                    item = json.loads(item)
                if custon_convert:
                    item = custon_convert(item)
                result.append(item)
            else:
                is_done = True
        return result