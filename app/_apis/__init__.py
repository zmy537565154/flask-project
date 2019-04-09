from app.extensions import api
from .firstApi import FirstApi

# 此处注册api
api.add_resource(FirstApi, '/hello')
