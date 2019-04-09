# -*- coding: utf-8 -*-

# Config里面算是通用配置,子类分别定义专属配置

import os

basedir = os.path.abspath(os.path.dirname(__file__))




class Config(object):
    pass
    '''
    此处为配置内容
    '''



class DevelopmentConfig(Config):
    DEBUG = True

    @staticmethod
    def init_app(app):
        pass


config = {
    'DevelopmentConfig':DevelopmentConfig
}