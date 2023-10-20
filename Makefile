install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black ./my_package/*.py 

lint:
	pylint --disable=R,C,locally-disabled --ignore-patterns=./my_package/test_.*?py ./my_package/*.py

test:
	python3 -m pytest -vv --cov=test_package ./my_package/test_*.py
		
all: install format lint test  