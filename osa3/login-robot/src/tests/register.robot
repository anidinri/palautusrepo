*** Settings ***
Resource  resource.robot
#Library ../AppLibrary.py
from entities.user import User

Test Setup  Create User And Input Login Command
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kissa  koirakoira3

Register With Already Taken Username And Valid Password
    Input Credentials  kissa  koirakoira3

Register With Too Short Username And Valid Password
    Input Credentials  ma  kallekallela123

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  matti12  kallekallela123

Register With Valid Username And Too Short Password
    Input Credentials  matti  kala

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  matti  mattimattimatti


*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kallekallela123
    Input Login Command

 Create User And Input New Command
    Create User  k  kallekallela123
    Input New Command