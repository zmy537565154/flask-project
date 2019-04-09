from flask import Flask
from conf.config import config
from app.extensions import *
from app.views import blueprint_config
from app._apis import *


def create_app(config_name='DevelopmentConfig'):
    '''
    封装创建方法
    :param config_name: 环境名
    :return: app应用
    '''
    # 创建app应用
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(config[config_name])

    # 额外初始化 我不用
    # config.get().init_app(app)

    # 加载扩展 我不用
    extension_config(app)

    # 注册蓝本
    blueprint_config(app)

    return app
