conda activate env portfolio
source .venv/bin/activate
python3 -m pytest main.py --alluredir=allure-results --headed
