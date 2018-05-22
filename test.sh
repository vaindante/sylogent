
export LANG=en_US.UTF-8

export URL=https://rc.sylogent.com/ps/Landing/Login.aspx

export PYTHONUNBUFFERED=1
export LOGGING_LEVEL=INFO
export PYTHONPATH="`pwd`"
export PYTHONDONTWRITEBYTECODE=1
export USE_LOCALHOST=1
export CHROME_DRIVER_PATH=./core/chromedriver

python py.test -m "smoke"