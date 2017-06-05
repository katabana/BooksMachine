from setuptools import setup

setup(name='booksmachine',
    version='0.16',    
	description='Module for quotes verification',
    url='https://github.com/AGHPythonCourse2017/zad3-katabana',
    author='Katarzyna Banaszak',
	author_email='katarzyna.bana@gmail.com',
    packages=['booksmachine'],
	entry_points={
		'console_scripts' : [
			'booksmachine = booksmachine:main']},
	include_package_data=True,
zip_safe=False)
