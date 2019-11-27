from setuptools import setup,find_namespace_packages

setup(
    name='connectcli',
    description = "app store connect api cli use apikey and issuer_id to authorize",
    url = "https://github.com/hepburnv/connectcli",
    version='1.0.2',
    author = "yuyuan yue",
    author_email = "last_yearv@163.com",
    license = 'MIT',
    include_package_data=True,
    exclude_package_data={'':['.gitignore']},
    package_dir={'': 'connect_apk'},
    packages=find_namespace_packages(where='connect_apk'),
    py_modules=['connectapi'],
    install_requires=[
        'Click',
        'requests',
        'authlib'
    ],
    scripts=['connect_apk/main.py','connect_apk/connectapi.py'],
    entry_points={
        'console_scripts': [
            'connectcli = main:cli'
        ]
    }
)