# 环境 Python 3

## virtualenv

安装
pip3 install virtualenv setuptools

1.创建一个独立的Python运行环境
virtualenv --no-site-packages venv

2.进入环境
source venv/bin/activate

3.退出环境
deactivate

4.编译
python setup.py install

5.运行
connectcli

6.打包
python setup.py sdist bdist_wheel

7.上传

安装twine

pip3 install twine

上传测试环境
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

上传正式环境
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

### 第三方库

pip3 install authlib

pip3 install requests

pip3 install Click