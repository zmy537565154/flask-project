from .main import main


# 蓝本 二维元组(蓝本,'路由')
DEFAULT_BLUEPRINT = (
    (main, ''),
)


# 注册函数
def blueprint_config(app):
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)
