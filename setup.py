from setuptools import setup,find_namespace_packages

setup(
    name='connectcli',
    version='1.0.0',
    package_dir={'': 'connect_apk'},
    packages=find_namespace_packages(where='connect_apk'),
    author = "yuyuan yue",
    author_email = "last_yearv@163.com",
    include_package_data=True,
    exclude_package_data={'':['.gitignore']},
    license = 'MIT',
    description = "app store connect api cli user apikey and issuer_id to authorize",
    url = "https://github.com/agony5/connectcli",
    install_requires=[
        'Click',
        'requests',
        'authlib'
    ],
    python_requires='>=3.6',
    scripts=['connect_apk/main.py','connect_apk/connectapi.py'],
    entry_points={
        'console_scripts': [
            'connectcli = main:cli'
        ]
    }
)