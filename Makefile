doctest:
	python3 -m doctest -v *.py

unittestBasic:
	python3 Tests.py
	
unittestNewTwist:
	python3 TestNewTwist.py

unittestMatrix:
	python3 MatrixTest.py

clean:
	rm -r -f *.pyc __pycache__
