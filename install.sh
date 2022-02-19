cp -f flaskenv-template.env .flaskenv
python3 -m venv venv
. venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt