from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in olla_academy/__init__.py
from olla_academy import __version__ as version

setup(
	name='olla_academy',
	version=version,
	description='Olla Website and Online Learning Apps for Frappe',
	author='Bantoo',
	author_email='devs@thebantoo.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
