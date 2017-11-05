#!/usr/bin/env python3

from flask_script import Manager
from flask_script.commands import Server, ShowUrls, Clean
from config import config
from webapp import create_app

app = create_app(config['dev'])

manager = Manager(app)

manager.add_command('runserver', Server())
manager.add_command('showurls', ShowUrls())
manager.add_command('clean', Clean())

if __name__ == '__main__':
    manager.run()
