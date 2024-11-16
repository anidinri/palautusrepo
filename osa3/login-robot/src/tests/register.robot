*** Settings ***
Resource  resource.robot
#Library ../AppLibrary.py
from entities.user import User

Test Setup  Create User And Input Login Command
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Create User  kissa  koira

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Output Should Contain  User with username kalle already exist

Register With Too Short Username And Valid Password
# ...

Register With Enough Long But Invalid Username And Valid Password
# ...

Register With Valid Username And Too Short Password
# ...

Register With Valid Username And Long Enough Password Containing Only Letters
# ...


*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command

Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command