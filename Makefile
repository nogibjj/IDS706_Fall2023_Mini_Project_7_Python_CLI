install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black ./yz674/*.py 

lint:
	pylint --disable=R,C,locally-disabled --ignore-patterns=./yz674/test_.*?py ./yz674/*.py

test:
	python3 -m pytest -vv --cov=test_package ./yz674/test_*.py
		
all: install format lint test  