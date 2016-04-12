django_settings = \
"""
DATABASES['default'] = ...
SESSION_ENGINE = ...
DEFAULT_FILE_STORAGE = ...
"""

class DjangoDeployment(Node):
	def upload_django_settings(self):
		with self.host.open('~/git/django-project/local_settings.py') as f:
			f.write(django_settings)

    def run_management_command(self, command):
    	with self.host.prefix(self.activate_cmd):
    		with self.host.cd('~/Documents/devs/banksecurity/'):
    			self.host.run('./manage.py %s' % command)

    def django_shell(self):
    	self.run_management_command('shell')

    def install_gunicorn(self):
    	self.install_package('gunicorn')

    def install_supervisord(self):
    	self.install_package('supervisor')

    def run_gunicorn(self):
    	self.run_management_command('run_gunicorn')