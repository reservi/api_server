
#!/bin/bash
function die() {
    echo "FATAL ERROR: $* (status $?)" 1>&2
    exit 1
}

# Fail on error
set -e

# Define some paths
current_path=$(pwd | sed -e "s/\n//")
script_path=$(dirname $0 | sed -e "s|^\.|${current_path}|")
# Get virtualenv path from command line argument, if it exists, or set to default
if [ $# == 1 ]
then
    virtualenv_path=$(echo $1 | sed -e "s|^\.|${current_path}|")
else
    virtualenv_path=${script_path}/.venv
fi

echo "virtualenv_path: ${virtualenv_path}"


cd ${script_path}

echo "Creating virtual environment with $python in ${virtualenv_path}"
python3 -m venv ${virtualenv_path} || die "Could not create virtual environment"

# Activate the new virtual environment so we can install things in it
echo "Activating virtual environment in ${virtualenv_path}"
source ${virtualenv_path}/bin/activate
echo "Python binary: $(which python)" -

echo "Upgrading pip"
pip install --upgrade pip --no-cache-dir

echo "Install stuff using: pip install -r requirements.txt"
pip install --trusted-host arm.lmera.ericsson.se -r requirements.txt --no-cache-dir

python setup.py install
