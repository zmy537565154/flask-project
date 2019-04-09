from flask_script import Manager
from flask_migrate import MigrateCommand
from app import create_app
import os

# 环境 此处直接默认为生产环境
# config_name = os.environ.get('CONFIG_NAME') or 'default'
# 创建app
app = create_app()

manager = Manager(app)


# manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
