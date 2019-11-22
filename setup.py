from setuptools import setup,find_packages

setup(
    name='connectcli',
    version='1.0.0',
    packages=find_packages(),
    author = "yuyuan yue",
    author_email = "last_yearv@163.com",
    description = "app store connect api cli user apikey and issuer_id to authorize",
    license = "MIT",
    url = "http://example.com/HelloWorld/",
    install_requires=[
        'Click',
        'requests',
        'authlib'
    ],
    entry_points='''
        [console_scripts]
        connectcli=connectcli.main:cli
    ''',
)