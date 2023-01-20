# Flask Simple Crud

## A simple crud using only flask and html, connected to a MySQL Database for storing user data, and some simple html templates to interact with the api to create, update and delete users.

## To test is nescessary:
### Have MySQL installed
## On MySQL prompt create your user and database
```
sudo mysql -u root
CREATE USER 'user'@'localhost';
GRANT ALL ON *.* TO 'user'@'localhost';
\q
mysql -u user -p
CREATE DATABASE simple_crud;

```

### Clone the repo and enter on the folder:
```
git clone git@github.com:GB255/flask_simple_crud.git
cd flask_simple_crud
```
### Install nescessary packages: 
```
pip install -r requirements.txt
```
### Execute the api: 
```
python3 api_app.py
```
### Access: http://127.0.0.1:5000
