# Local Password Manager

Manage locally all your passwords !

## Introduction

A password is defined as the collection of a name, an identifier (which can be empty) and a password.

Passwords are encrypted in a file in the root directory. You will be asked to create a password as you launch the 
program for the first time which will be used to encrypt and decrypt data.


## How to install

- First of all, download the repository :

        git clone https://github.com/jpennors/local_password_manager

- Create the file `env.ini` by copy pasting the file `env.example.ini` in `config` folder.

- Download all dependencies :

        pip install requirements.txt

- Just launch the program with the command `python password.py` ! As you launch it for the first time the program will ask you to give a password. The latter 
will be the one that protect all of your passwords. Use a **complex** one and remember it !

- The program will generate a hash of your password. You will need to copy paste this hash (in fact the one will be
already copy in your clipboard) in the file `env.ini` that
you just created from `env.example.ini` in your `config` folder.

- Just relaunch the program, you will need to enter your password ! Default execution is an interactive program to manage your 
password. You can also use arguments in your command (see below).

## Command args

- Launch interactive mode (default one) :

        python password.py -interactive

- List all your passwords (doesn't display credentials):

        python password.py -list

- Consult credentials of a password :

        python password.py -get -n=name_of_your_password

Argument `-n=` is optional. In case you don't fill it, passwords list will be displayed and you will be able to 
select the one you want to consult.

- Add a new password :

        python password.py -add -n=name_of_your_password -i=identifier_of_password -p=password_itself

Arguments `-n=`, `-i=` and `-p=` are optional. In case you don't fill some you will be asked to fill missing 
information. 

- Update a password :

        python password.py -update -n=name_of_your_password -i=identifier_of_password -p=password_itself

Arguments `-n=`, `-i=` and `-p=` are optional. In case you don't fill some you will be asked to fill missing 
information. 

- Remove a password :

        python password.py -remove -n=name_of_your_password

Argument `-n=` is optional. In case you don't fill it, password list will be displayed and you will be able to 
select the one you want to remove.


### Remaining tasks

- Improve error messages, especially since command arguments have been added

- Creation of a protected file such as a ZIP file with the app password or a protected file which requires
admin permission (behaviour may change depending on OS)

- Create a signal to get back to the menu at any time in interactive mode

- Make the PasswordManager class a Singleton (like Login class)

