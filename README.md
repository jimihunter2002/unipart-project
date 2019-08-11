This README details the steps and requirements for running the tests provided in this project
run the command below to install the requirments needed

Assumptions:
1. python 3.6 or greater is installed
2. pip is installed
3. test will be run on a windows machine.

pip install -r requirements.txt

download selenium standalone server and include the jar in System Path if needed
download chrome driver and also include the executable in System Path

unzip the project

and once all the requiremenst above have been met

to run test module individually

from the root of the project folder (unipart) run the command
1. "pytest -s -v .\amazon\tests\<testfile.py> --browser chrome"

to run tests as suite
2. "pytest -s -v .\amazon\tests --browser chrome"

3. To run test for the Fizz Buzz game run the command below
 pytest -v -s .\fizzbuzz\test
