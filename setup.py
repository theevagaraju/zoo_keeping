from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in zoo_keeping/__init__.py
from zoo_keeping import __version__ as version

setup(
	name='zoo_keeping',
	version=version,
	description='zoo management',
	author='raju',
	author_email='raju@tektician.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
