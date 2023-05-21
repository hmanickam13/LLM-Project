# upgrade pip
pip install --upgrade pip

# install project dependencies (refers to requirements.txt)
cat requirements.txt | sed -e '/^\s*#.*$/d' -e '/^\s*$/d' | xargs -n 1 python -m pip install