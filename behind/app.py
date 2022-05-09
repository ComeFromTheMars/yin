from flask import Flask, jsonify, request
from flask_cors import CORS
import re

# request.method 判断是什么请求方式
# request.form是一个字典存储的是前端提交的表单键值对
# redirect("重定向网页")
# url_for("重定向方法")
# make_response(数据) 返回数据到前端
# json.dumps(dir)将python字典转化为json数据
# jsonify(数据)返回到前端
# abrot 在网页返回错误
# jianjia2 模板
# 渡中心性


app = Flask(__name__)

CORS(app)
from Curl_Graphy import return_dict, getnode, f

# 设置编码
app.config['JSON_AS_ASCII'] = False
ip6_regex = (
    r'(^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$)|'
    r'(\A([0-9a-f]{1,4}:){1,1}(:[0-9a-f]{1,4}){1,6}\Z)|'
    r'(\A([0-9a-f]{1,4}:){1,2}(:[0-9a-f]{1,4}){1,5}\Z)|'
    r'(\A([0-9a-f]{1,4}:){1,3}(:[0-9a-f]{1,4}){1,4}\Z)|'
    r'(\A([0-9a-f]{1,4}:){1,4}(:[0-9a-f]{1,4}){1,3}\Z)|'
    r'(\A([0-9a-f]{1,4}:){1,5}(:[0-9a-f]{1,4}){1,2}\Z)|'
    r'(\A([0-9a-f]{1,4}:){1,6}(:[0-9a-f]{1,4}){1,1}\Z)|'
    r'(\A(([0-9a-f]{1,4}:){1,7}|:):\Z)|(\A:(:[0-9a-f]{1,4}){1,7}\Z)|'
    r'(\A((([0-9a-f]{1,4}:){6})(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3})\Z)|'
    r'(\A(([0-9a-f]{1,4}:){5}[0-9a-f]{1,4}:(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3})\Z)|'
    r'(\A([0-9a-f]{1,4}:){5}:[0-9a-f]{1,4}:(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)|'
    r'(\A([0-9a-f]{1,4}:){1,1}(:[0-9a-f]{1,4}){1,4}:(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)|'
    r'(\A([0-9a-f]{1,4}:){1,2}(:[0-9a-f]{1,4}){1,3}:(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)|'
    r'(\A([0-9a-f]{1,4}:){1,3}(:[0-9a-f]{1,4}){1,2}:(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)|'
    r'(\A([0-9a-f]{1,4}:){1,4}(:[0-9a-f]{1,4}){1,1}:(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)|'
    r'(\A(([0-9a-f]{1,4}:){1,5}|:):(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)|'
    r'(\A:(:[0-9a-f]{1,4}){1,5}:(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)')
url = r"(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?"


def ipv6_check(addr) -> bool:
    '''
    模式串匹配ipv6
    '''
    return bool(re.match(ip6_regex, addr, flags=re.IGNORECASE))


@app.route('/')
def hello_world():
    dir = return_dict()
    return jsonify(dir)


@app.route('/match')
def matchnode():
    print("开始匹配！！")
    a = request.values.get('ip')
    a = a.strip().split('?')
    print(a)
    if len(a) == 1:
        if ipv6_check(a[0]):
            return jsonify(getnode(a[0], "ip"))
        elif a[0] == "普通节点":
            return jsonify(getnode("1", "kind"))
        elif a[0] == "终端节点":
            return jsonify(getnode("2", "kind"))
        elif a[0] == "中转节点":
            return jsonify(getnode("3", "kind"))
        elif a[0] == "匿名节点":
            return jsonify(getnode("4", "kind"))
        elif a[0] == "地标节点":
            return jsonify(getnode("5", "kind"))
        elif '学' in a[0] or bool(re.match(url, a[0])):
            return jsonify(getnode(a, "post"))
        else:
            return jsonify([])
    elif len(a) == 2:
        return jsonify(f(a[0], a[1]))


if __name__ == '__main__':
    app.run()
