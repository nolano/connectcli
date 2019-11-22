from setuptools import setup,find_packages

setup(
    name='connectcli',
    version='1.0.0',
    packages=find_packages(),
    author = "yuyuan yue",
    author_email = "last_yearv@163.com",
    description = "app store connect api cli user apikey and issuer_id to authorize",
    url = "https://github.com/agony5/connectcli",
    install_requires=[
        'Click',
        'requests',
        'authlib'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points='''
        [console_scripts]
        connectcli=connectcli.main:cli
    ''',
)