#coding: utf-8
__author__ = "anphyLong"
__date__ = " 2018/05/04"


from functools import wraps
from flask import g, request, jsonify

args_methods = {"GET", "DELETE"}


def auth_params(**methods):
    def wrapper(func):
        @wraps(func)
        def auth_params(*args, **kwargs):
            try:
                method = request.method
                if method in methods:
                    params = request.args if method in args_methods else request.form or request.json
                    print("before:", params)
                    if set(methods[method]).issubset(set(params or [])):
                        g.params = params.to_dict() if type(params) != dict else params
                        return func(*args, **kwargs)
                    return jsonify({"sts": 0, "msg": "缺乏参数"})
                return func(*args, **kwargs)
            except Exception as e:
                return jsonify({"sts": -1, "msg": "缺乏参数"})
        return auth_params
    return wrapper


def hanle_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return jsonify({"sts": -1, "msg": "缺乏参数"})
    return wrapper
