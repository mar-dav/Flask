# Flask
# Vend.io Project - 2021

## Marsdin Davidson

Proof of Concept Video: https://drive.google.com/file/d/10EphHlJXzN-AjDw6vaX1HYH3tjzOc8tb/view?usp=sharing

Department

Rev: 01

Date:April 6th, 2021


## Table of Contents

- Code Checklist
- Project Overview:
- Standards:
- Objectives:
- Requirements/Task(s):
- Outline the steps/plan for your project:
- Summarize what you learned:
- Reference


## Code Checklist

Check list for all files that you will use in yourcode:


## Webpages:

1. addfunds.html
2. balance.html
3. dashboard.html
4. gamelistings.html
5. games.html
6. index.html
7. inventory.html
8. layout.html
9. newlist.html
10. newwallet.html
11. nologin.html
12. register.html
13. result.html
14. resultredir.html

## API Files:

flask_main.py (All api calls are in this file)
  i. btccost & ethcost (requests.get method)
  ii. index.html (‘/’) calls btccost and ethcost
  iii. login.html (‘/login’) post/get api call. Requestinglogin.html via get
will return nologin.html which is a custom 404 page made.
Requesting login.html via post will call select statements for my sqlite
database to validate the username and password. There's a conditional
on dashboard.html

iv. Dashboard (‘/dashboard’) Post/Get calls. If websiterequested by get
then return nologin.html, but if not return dashboard.html

v. Games (‘/games’). Connect to the sqlite database and store it in games
and the sql table to games.html to be processed and displayed
Games.html has a for loop which runs via the python interpreter
vi. Newlist (‘/newlist’) page to create a new listingto post an item. Uses
the games table to generate radio buttons so the user can select which
game he wants.

vii. No login. Display 404 screen

viii. Post register – form handler to add user to sql table

ix. Create wallet (‘/createwallet’). Get the uid from the provided login and
pass the uid to the wallet table when creating the listing so that it is
linked to that user. Any error will be caught and an error message will
pop up on the result.html page.

x. Purchase (‘/purchase’) if user select an item from the drop down they
can add it to the items table which is linked via uid and view on the
inventory page.

xi. Balance (‘/balance’) view the wallets that a user creates by uid. Uid is
passed from the dashboard screen via GET.

xii. Inventory (‘/inventory’) select all the data fromthe inventory table and
pass it to inventory.html.

xiii. List by game (‘/listbygame’) view user submitted listings and sort by
game. GID is passed via GET.

xiv. Addfunds (‘/addfunds’). If this page is reached via Post then grab the
live price for bitcoin or ethereum and convert user balance to the
crypto type in their wallet. There is an if statement to display the
balance in bitcoin or ethereum depending on which crypto they chose
for that wallet. All data is passed to the html file.If there is an error,
display an error message.

xv. Fundspost (‘/fundspost’) update the wallet with the dollar amount the
user provides using the sql update function. This definition takes the
current value and adds the user submitted value to the wallet.

xvi. Addlist (‘/addlist’) add a listing with the user submitted price. Subtract
the balance from the wallet when submitting the listing then use a sql
insert into function.

C. Database:

1. wallet
2. listing
3. users
4. game
5. items

## vend.io

## Project Overview:

This project simulates a crypto trading marketplace.Users can register, view listings by game,
add simulated bitcoin or ethereum wallets and be ableto post listings for items in that game.

## Standards:

● Handle basic SQL and python errors.
● Create an SQL database
● Learn how to make python and sql talk to one another

## Objectives:

● Create marketplace where users can sign in, createwallets and listings.
● View supported games.
● View live crypto prices.
● Use flask to generate dynamic web pages.

## Requirements/Task(s):


Task 1- Creating a functional website using pythonand a sql database.
Task 2 – Create an sql database with 5 tables or higher
Task 3 – Use 8 html pages or higher.

## Project Details:

- Show the communication protocols between each module and the response page
- btccost & ethcost (requests.get method)
- index.html (‘/’) calls btccost and ethcost
- login.html (‘/login’) post/get api call. Requestinglogin.html via get will
return nologin.html which is a custom 404 page Imade. Requesting
login.html via post will call select statements formy sqlite database to

validate the username and password. There is a conditional on
dashboard.html

- Dashboard (‘/dashboard’) Post/Get calls. If websiterequested by get then
return nologin.html, but if not return dashboard.html


- Games (‘/games’). Connect to the sqlite database andstore it in games and the sql
    table to games.html to be processed and displayed.Games.html has a for loop which
    runs via the python interpreter
- Newlist (‘/newlist’) page to create a new listingto post an item. Uses the
games table to generate radio buttons so the usercan select which game he
wants.
- Nologin. Display 404 screen
- Postregister – form handler to add user to sql table.Takes values from username,
    password, and email and uses them in an insert intostatement on the server.
- Create wallet (‘/createwallet’). Get the uid fromthe provided login and pass the uid to
    the wallet table when creating the listing so thatit is linked to that user. Any error will
    be caught and an error message will pop up on theresult.html page. This route is a
    POST function
- Purchase (‘/purchase’) if a user selects an item from the drop down they can add it to
    the items table which is linked via uid and view onthe inventory page.
       ▪ Balance (‘/balance’) view the wallets that a usercreates by uid. Uid is
          passed from the dashboard screen via GET.
- Inventory (‘/inventory’) select all the data fromthe inventory table and pass it to
    inventory.html.
       ▪ Listbygame (‘/listbygame’) view user submitted listingsand sort by game.
          GID is passed via GET.

- Addfunds (‘/addfunds’). If this page is reached viaPOST then grab the
live price for bitcoin or ethereum and convert userbalance to the crypto
type in their wallet. There is an if statement todisplay the balance in
bitcoin or ethereum depending on which crypto theychose for that wallet.
All data is passed to the html file. If there is anerror, display an error
message.



▪ Fundspost (‘/fundspost’) update the wallet with the dollar amount the user
provides using the sql update function. This definitiontakes the current
value and adds the user submitted value to the wallet.

▪ Addlist (‘/addlist’) add a listing with the user submittedprice. Subtract the
balance from the wallet when submitting the listingthen use a sql insert
into function.

- Support the illustration with a screenshot from thewebpage for your project
- Show the prevented error and how you handle the project.

## Outline the steps/plan for your project:

1. Illustrate database connections
2. Create database connections


3. Create sqlite database then create project.

## Summarize what you learned:

I learned how to use flask to create html websites.I also learned how to use a sqlite database and
learned that it was much easier than making a regulardatabase.

## Reference

https://www.youtube.com/watch?v=mqhxxeeTbu


