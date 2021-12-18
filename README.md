# T3A3_asx_app
A web application to view and follow financial data from ASX listed companies.

## Installation:

To install this application execute the following commands from your terminal: 

1. Pull the source code from the repository: 
`git clone https://github.com/l-j-g/T3A3_asx_app.git`

2. Navigate to the installation directory e.g. :
`cd ./T3A3_asx_app`

3. Create a virtual python environment to hold additional packages 
For macOS and GNU systems: 
 `python -m venv env`
For windows systems:
 `py -m venv env`
4. Activate the python virtual environment: 
For macOS and GNU systems: 
 `source env/bin/activate`
For windows systems:
 `.\env\Scripts\activate`
5. Install the nessecary requirements for the application 
For macOS and GNU systems: 
 `python3 -r pip install requirements.txt`
For windows systems:
 `py -r pip install requirements.txt`

## Requirements:

- [flask](): Python web framework

- [postgresql](https://www.postgresql.org/docs/14/index.html): open source object-relational database management system

- [psycopg2](https://www.psycopg.org/docs/): postgreSQL adapter for Python.

- [jinja](https://jinja.palletsprojects.com/en/3.0.x/): HTML templating engine for Python

- [marshmallow](https://marshmallow.readthedocs.io/en/stable/): library for converting datatypes to and from Python objects.

- [werkzeug]()

## Purpose:

The purpose of this application is to demonstrate web application development with create, read, update, delete (CRUD) capabilities. A full stack development framework that provides a Data, Application and Presentation layer has been provides utilising python, flask and postgresql. It has been developed in completion of the requirements of Term 3 Assignment 3 as a part of the Code, Cloud and Cyber course at CoderAcademy.

The application allows users to view and follow fundamental financial data for companies that are publicly listed on the Australian Stock Exchange. Users are able to register persistent accounts on the site, add selected companies to their portfolio and view the portfolios of other users on the site. Furthermore, the application demonstrates functionality to preform data aggregation and validation in order to assist in data interpretation and prevent integrity errors.

### List of Pages and Functionality:

- **Home**: Landing page for the site, providing general information and directions.
- **Users Index**: Displays an index of all users that have registered on the site
- **User Profile**: The public facing profile of each user registered on the site, displaying information about the users account
- **User Account**: Allows users to change account settings
- **Register**: Registration of new users
- **Sign In**: Login and validation of existing users credentials
- **Tickers Index**: List of companies that the website provides data for
- **Ticker Details**: Detailed fundamental financial data for specific listed company.

### Entity Relationship Diagram:

## Validation of Fields

This application utilises the `marshmallow` packages to preform validation of input data. Further field integrity is provided by SQL domain, entity and referential constraints that have been implemented at schemas through the `SQLAlchemy` package.

### Users

**username**:

SQL constraints: string, unique, not null, length < 200.

usernames are validated to ensure that they conform to the following policy:

- at least 6 characters, less then 200 characters.
- 1 upper case letter
- 1 lower case letter
- 1 digit.

**password**:

SQL constraints: string, not null, length < 200.

passwords are validated to ensure that they contain at least three characters from the set `[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._]`.

**id**:

SQL constraints: integer, primary_key

### Tickers

**ticker_id**

SQL constraints: string, primary_key





## Security 



- Passwords will not be stored as plaintext in database.
- Password will be stored as hash which is irreversible to plaintext. (one way hash).
- With given hash attacker cannot guess plaintext.
- Each user password will be hashed with salt to mitigate rainbow table attacks; Just in case if database got compromised.


Professional obligations
Ethical obligations
Example of legal obligations


## TODO

Add more tickers
Add pagination
Add info 1-1 relation
Add password validation
Finish readme
Fix images

