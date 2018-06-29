
export LANG=en_US.UTF-8

export URL=https://rc.sylogent.com/ps/Landing/Login.aspx

export PYTHONUNBUFFERED=1
export LOGGING_LEVEL=INFO
export PYTHONPATH=`pwd`
export PYTHONDONTWRITEBYTECODE=1
export USE_LOCALHOST=1
export CHROME_DRIVER_PATH=./core/chromedriver
export LOGIN=sylogent.admin@sylogent.com
export PASSWD=AnjuSoftware2018

./venv1/bin/python ./venv1/bin/ py.test -m "test_01" --basetemp=../../scenarios