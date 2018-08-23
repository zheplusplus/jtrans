import src
from setuptools import setup

requirements = [
    'click==6.7',
    'requests==2.19.1',
    'pyquery==1.4.0',
]

setup(
    name='jtrans',
    version=src.__version__,
    author='Neuron Teckid',
    author_email='lene13@gmail.com',
    license='MIT',
    keywords='',
    url=src.REPO,
    description='',
    packages=['src'],
    long_description='Visit ' + src.REPO + ' for details please.',
    install_requires=requirements,
    zip_safe=False,
    entry_points=dict(
        console_scripts=[
            'jtrans-cli=src.console:main',
        ], ),
)
