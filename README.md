# Adaptive Lab's Technical Test #

# Introduction #
Web application that displays tweets about Coke.

The following instruction have only been executed on Mac OS X.

## Execution ##

### Requisites ###
The following software is needed to execute this application:
* Python 2.6
* [virtualenv](http://pypi.python.org/pypi/virtualenv>)
* [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/)

### Python Virtual Environment ###
We deploy this application into it's own virtual environment therefore you will 
need to do the same. Install & Activate the virtualenv (this assumes you are in 
the root of the application folder using a cli):

        easy_install virtualenv
        mkdir ~/.virtualenvs
        cd ~/.virtualenvs
        virtualenv adaptivelab
        source ~/.virtualenvs/adaptivelab/bin/activate

### Install Python Packages ###
This assumes you are in the root of the application folder using cli:

        cd src
        while read line; do easy_install -ZU $line; done < install-requires.txt
        while read line; do easy_install -ZU $line; done < install-test-requires.txt
        
### Running Application ###
Execute the following to get the application up and running (assumes you are in 
the root of the project):

        cd src/adaptivelab
        python setup.py develop
        python manage.py syncdb
        python manage.py runserver
        
### Running Unit Tests ###
This assumes you are in the root of the project:

        cd src/adaptivelab
        python setup.py develop
        python manage.py test
        
## Database ##
The database is put into a temporary folder that is printed to the console when 
the application is started using python manage.py runserver. Using sqlite3 you 
can then query the table coke_tweet to see the data captured.
