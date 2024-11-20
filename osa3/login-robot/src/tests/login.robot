*** Settings ***
Resource  resource.robot
#Library ../AppLibrary.py
from entities.user import User

Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123


Login With Incorrect Password
    Input Credentials  kalle  kissa
    Output Should Contain  Invalid username or password

Login With Nonexistent Username
    Input Credentials  kissa  kalle123
    Output Should Contain  Invalid username or password

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kallekallela123
    Input Login Command
