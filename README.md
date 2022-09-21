# OnlyProfits
This project will use the Polygon API to get the prices of stocks and/or cryptocurrencies.

## Project Aims
This project aims to:
* Keep track of Stock and/or Crypto data
* Store this data in a database
* Create a web interface to display this data
* Allow users to create an account which can save favourite stocks and/or cryptocurrencies

## Running the project
To run the project, you will need to have Python 3+ installed. You will also need to install the requirements in the requirements.txt file. To do this, run the following command while in the project directory (you may need to use `pip3` instead of `pip` depending on your system):
```
pip install -r requirements.txt
```
The project can then be run by running the following command (you may need to prepend this with `python` or `python3` depending on your system):
```
manage.py runserver
```


## Running Tests
To run the tests, run the following command (again you may need to prepend this with `python` or `python3` depending on your system):
```bash
manage.py test onlyProfits_app
```
