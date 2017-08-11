# mp-boshrelease

A practice to create a BOSH release.

## Prerequisites

* [BOSH CLI v2](https://bosh.io/docs/cli-v2.html#install)
* [Prepare local blobstore](#download-blobs)

## Download blobs

```
cd /tmp

wget https://www.python.org/ftp/python/2.7.11/Python-2.7.11.tgz
wget https://pypi.python.org/packages/py2.py3/w/wheel/wheel-0.29.0-py2.py3-none-any.whl
wget https://pypi.python.org/packages/py2.py3/p/pip/pip-8.1.1-py2.py3-none-any.whl
wget https://pypi.python.org/packages/py2.py3/s/setuptools/setuptools-20.9.0-py2.py3-none-any.whl
wget https://pypi.python.org/packages/py2.py3/v/virtualenv/virtualenv-15.0.1-py2.py3-none-any.whl
wget -O cf-cli_6.26.0_linux_x86-64.tgz "https://cli.run.pivotal.io/stable?release=linux64-binary&version=6.26.0&source=github-rel"
wget -O /bosh-cli-2.0.28-linux-amd64 "https://s3.amazonaws.com/bosh-cli-artifacts/bosh-cli-2.0.28-linux-amd64"

bosh add-blob /tmp/Python-2.7.11.tgz python_2.7/Python-2.7.11.tgz
bosh add-blob /tmp/wheel-0.29.0-py2.py3-none-any.whl python_2.7/wheel-0.29.0-py2.py3-none-any.whl
bosh add-blob /tmp/pip-8.1.1-py2.py3-none-any.whl python_2.7/pip-8.1.1-py2.py3-none-any.whl
bosh add-blob /tmp/setuptools-20.9.0-py2.py3-none-any.whl python_2.7/setuptools-20.9.0-py2.py3-none-any.whl
bosh add-blob /tmp/virtualenv-15.0.1-py2.py3-none-any.whl python_2.7/virtualenv-15.0.1-py2.py3-none-any.whl
bosh add-blob /tmp/cf-cli_6.26.0_linux_x86-64.tgz cli/cf-cli_6.26.0_linux_x86-64.tgz
```
