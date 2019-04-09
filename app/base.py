# coding: utf-8
from flask_restful import Resource, reqparse

from flask import request
import json
from .common.log_ import logger
import flask_restful


class MyRequestParser(reqparse.RequestParser):
    """自定义参数请求"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class BaseResource(Resource):
    default_help = '不是一个有效值'

    # tid_file_dir = Config._REPORT_FILES_DIR

    def __init__(self, *args, **kwargs):
        self.parser = MyRequestParser()
        logger.info(request.remote_addr + ' >>> 请求参数：' + str(request.json))
        super().__init__(*args, **kwargs)


# 自定义请求体检验
class MyBaseResource(Resource):
    def __init__(self, *args, **kwargs):
        pass

    def get_params(self):
        try:
            params = request.form
            if not params:
                params = json.loads(request.data.decode())
        except:
            flask_restful.abort(400, message='请求体格式有误')
        logger.info(request.remote_addr + ' >>> 请求参数：' + str(params))
        return params
