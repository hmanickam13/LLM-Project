# create python venv named venv
python3.10 -m venv ./ghcproject

# activate venv
source ghcproject/bin/activate

# upgrade pip
pip install --upgrade pip

# install project dependencies (refers to requirements.txt)
cat requirements.txt | sed -e '/^\s*#.*$/d' -e '/^\s*$/d' | xargs -n 1 python -m pip install