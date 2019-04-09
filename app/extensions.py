from flask_restful import Api
from flask_moment import Moment
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
import pymysql
# from flask_session import Session

# 创建扩展实例
api = Api()
moment = Moment()
# db = SQLAlchemy()
# migrate = Migrate()


# 初始化
def extension_config(app):
    api.init_app(app)
    moment.init_app(app)
    # db.init_app(app)
    # migrate.init_app(app, db)

