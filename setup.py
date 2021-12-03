from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='SnakeGameMaker',
    version='0.1.1',
    description='It is use to built SnakeGame',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Joshua Lowe',
    author_email='josh@edublocks.org',
    license='MIT',
    classifiers=classifiers,
    keywords='SnakeGameMaker',
    packages=find_packages(),
    install_requires=['']
)