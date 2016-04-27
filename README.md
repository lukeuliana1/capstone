# Table of Contents
  * [Useful Links](#useful-links)
  * [Prerequisites](#prerequisites)
  * [Launch Project](#launch-project)
  * [Localhost Setup](#localhost-setup)
  * [Populate Database with Fake Data](#populate-database)
  * [How to Create Superuser (admin)](#createsuperuser)
  * [MySQL Notes](#mysql-notes)
  * [Virtualenv Notes](#virtualenv-notes)
  * [Adding Code Instructions](#adding-code)

## Intro
Hello New Capstone Team :) We (Last Capstone Team) prepared this Readme file, so it would be easier for you to pick up this project.
Before starting working on the project !Please! do some research about Django and Front-end tools that you are going to use (otherwise you would probably have a bad time working on it):

* [Django Girls](https://djangogirls.org/ "Django Girls") 
   <p>Shortest possible Into to Django
* [Django Docs](https://docs.djangoproject.com "Django Docs")
   <p>Always refer to Docs if you have problems
* [My Dev Guide written for ENGL 202C](https://www.dropbox.com/s/4fwvmfffze3qiyz/Web%20Development%20Guide%20for%20College%20Students.pdf?dl=0 "Dev Guide")
   <p> Covers all Front-end and Back-end tools that you are going to use

Also, read all comments in the code, and follow instuctions below.

##### Good Luck!

P.S. Feel free to delete this intro if needed

## Useful Links<a id="useful-links"></a>
1. [Trello board for this repo](https://trello.com/b/fa1VjgZB/captostonetracker "Trello board for this repo")
2. [Automated Code Review](https://www.quantifiedcode.com/ "QuantifiedCode")
3. [Live Interactive Cross Browser Testing](https://www.browserling.com/ "Browserling")
4. [Analyze Web Site Speed] (https://gtmetrix.com/ GTmetrix)

## Prerequisites<a id="prerequisites"></a>
#### OSX/Linux
* Python 3.4
* Pip (should be installed with python 3.4 installation)
* Virtualenv (pip3 install virtualenv)
* Virtualenvwrapper (pip3 install virtualenvwrapper)
* MySQL
* NodeJS (NPM)

#### Windows
##### Be sure to add python34 and python34/Scripts to you PATH
* Python 3.4
* Pip ( should be installed with the python3.4 installation)
* Virtualenv (pip3 install virtualenv)
* Virtualenvwrapper (pip3 install virtualenvwrapper-win)
* MySQL
* NodeJS (NPM)

## Launch Project<a id="launch-project"></a>
1. Navigate into capstone repo:
   <p>`$ cd capstone`
2. Pull latest updates from Github repo:
   <p>`$ git pull`
3. Install gulp and bower dependencies:
   <p>`$ sudo npm install && bower install`
   <p>If bower.json was updated follow step 3, otherwise skip it
4. Start Gulp:
   <p>`$ gulp`
5. Open new terminal
   <p>
6. Activate virtual environment:
   <p>`$ workon capstoneTracker`
7. Install package dependencies:
   <p>`$ pip install -r requirements.txt`
   <p>If requirements.txt updated follow step 7, otherwise skip it
8. Navigate into capstoneTracker directory:
   <p>`$ cd capstoneTracker`
9. Makemigrations for database:
   <p>`$ ./manage.py makemigrations`
10. Migrate database (update database):
   <p>`$ ./manage.py migrate`
11. Launch the server:
   <p>`$ ./manage.py runserver`


## Localhost Setup<a id="localhost-setup"></a>
1. Clone the repository:
   <p>`$ git clone https://github.com/yeralin/capstone.git capstone`

2. Navigate into capstone repo:
   <p>`$ cd capstone`

3. Create Virtual Environment Wrapper using Python 3.4:
   <p>`$ mkvirtualenv -p python3.4 capstoneTracker`

4. Go into you're local environment if not already there:
    <p>`$ workon capstoneTracker`
    <p>`(capstoneTracker)$ ` should appear at the start of your command prompt

5. Install all the requirements:
  <p>`$ pip3 install -r requirements.txt`

6. Create local database
    <p>`$ mysql -u root`
    <p>`$ create database capitalonecapstone;`
    <p>`$ quit`

7. Set up the database: (for windows do not include ./)
    <p>`$ ./capstoneTracker/manage.py makemigrations`
    <p>`$ ./capstoneTracker/manage.py migrate`

8. Install npm packages
    <p>`$ sudo npm install`

## Populate Database with Fake Data For Testing <a id="populate-database"></a>
    When you finished Localhost Setup Step you can follow this instructions
1. Call Django Shell and Pass Prepared script into the shell:
    <p>`./manage.py shell < scripts/PopulateDatabaseWithFakeData.py`
<br>
P.S. Do not try to edit PopulateDatabaseWithFakeData.py unless you already carefully read the code and you know what you are doing
<br><br>
P.P.S. All student users have following account credentials: FirstnameLastname@gmail.com:123 <br>
       All employee users have following account credentials: FirstnameLastname@capitalone.com:123

## How to Create Superuser (admin) <a id="createsuperuser"></a>
<p>In terminal type `./manage.py createsuperuser` and follow steps

## MySQL Notes <a id="mysql-notes"></a>
* When creating the root account if asked to create a root password, you must
 remove the root password in order to run the syncdb and migrations call.
  <p>`$ mysql -u root -p`
  <p>enter your password
  <p>`SET PASSWORD FOR root@localhost=PASSWORD('');`

* In order to use the mysql -u root, be sure to start your mysql server first. To start or stop the server use these commands
  <p>`$ mysql.server start`
  <p>`$ mysql.server stop`

##Virtualenv Notes <a id="virtualenv-notes"></a>
* If you are having issues running the mkvirtualenv or workon commands, make sure you have your vitrual env python and variable are set correctly. Adding these three lines to your .bash_profile should do the trick:
<p> `export WORKON_HOME=$HOME/.virtualenvs`  (This should be set to where ever your .virtualenvs directory is)
<p> `export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3` (This should be set to where ever your Python3 is located)
<p> `source /usr/local/bin/virtualenvwrapper.sh` (This should be where ever your virtualenvwrapper.sh can be found)
* In order to stop working within your virtualenv just type deactivate in your command prompt

## Adding code<a id="adding-code"></a>
Once you have completed your additions to files run the make file to check if your
code can be committed. Your code will be checked against the pep8 standards and
a code coverage check will be run. You want to conform to all standards and
have 100% code coverage.
