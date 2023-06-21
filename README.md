
# About the project

Python application for an KFC database. Project for the curricular unit of DataBases.

#  Reference

- [PyMySQL](https://pymysql.readthedocs.io/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Jinja templates](https://jinja.palletsprojects.com/en/3.0.x/)
- [Eduardo R. B. Marques](https://www.dcc.fc.up.pt/~edrdo/), DCC/FCUP


# Installation

## Python 3 and pip 

You must have Python 3 and the pip package manager installed. You can
install them under Ubuntu for example using:

```
sudo apt-get install python3 python3-pip
```

## Python libraries

```
pip3 install --user Flask==1.1.4 PyMySQL==1.0.2 cryptography==36.0.0
```


# Database configuration 

Edit the `db.py` file with respect to your DB configuration, modifying the `DB` (database name), `USER` (user name) and `PASSWORD` (user password) parameters.

Test the access by running:

```
python3 test_db_connection.py NAME_OF_TABLE
```

# Execution

Start the application by running `python3 server.py` and interact with it
by opening a window in your browser with the address [__http://localhost:9001/__](http://localhost:9001/)



