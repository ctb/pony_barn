import sys
from base_django import DjangoBuild
from pony_build import client as pony

class PonyBuild(DjangoBuild):

    def __init__(self):
        super(PonyBuild, self).__init__()
        self.repo_url = "git://github.com/ericholscher/django-kong"
        self.name = "django-kong"
        self.package_name = 'kong'
        self.required = ['django', 'twill']
        self.installed_apps = ['kong']

    def define_commands(self):

        self.commands = [ pony.GitClone(self.repo_url),
                     pony.BuildCommand([self.context.python, 'setup.py', 'install'], name='Install'),
                     pony.BuildCommand([self.context.djangoadmin, 'syncdb', '--noinput', '--settings', 'django_pony_test_settings'], name='Syncdb'),
                     pony.TestCommand([self.context.djangoadmin, 'test', self.package_name, '--settings', 'django_pony_test_settings'], name='run tests')
                     ]

if __name__ == '__main__':
    build = PonyBuild()
    sys.exit(build.execute(sys.argv))