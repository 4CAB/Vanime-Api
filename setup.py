from setuptools import setup
import os

class Configure():
	os.system('chmod +x $PWD/Vanime/vanime.py')
	os.system('sudo ln -s $PWD/Vanime/vanime.py /usr/local/bin/vanime')


setup(name='Vanime',
      version='0.1',
      description='Api de animeflv.net rápida, sencilla y accesible desde cualquier \
      emulador de terminal',
      url='https://github.com/4CAB/Vanime-Api',
      author='Matteus',
      author_email='trustmagali@gmail.com',
      license='MIT',
      packages=['Vanime', 'Vanime.utils'],
      zip_safe=False,
      cmdclass={'configure': Configure},
      install_requires=[
        "bs4==0.0.1",
        "cloudscraper==1.2.60",
        "lxml==4.9.1",
        "requests==2.28.1",
        "rich==12.5.1",]
)
