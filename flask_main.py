from flask import render_template, url_for, Flask, request
import sqlite3 as sql
import sys
import babel.numbers
import json
import requests
from bs4 import BeautifulSoup
app =  Flask(__name__)
# Q1- Using the database, and tables that you created in LAB08, deploy python interface to read these data and display each table on page.
# Q2- Add to each page option for inserting a new data.
#conn = sql.connect("database.db")
# print("opened db successfully")
# c = conn.cursor()
#cursor = conn.execute("SELECT * from emp")
# conn.execute('''CREATE TABLE phonebook
#             (phone_no text PRIMARY KEY,
#             name text NOT NULL,
#             addr text NOT NULL,
#             social_media text NOT NULL
#             );''')
# conn.execute('''CREATE TABLE EMP
#             (empno integer PRIMARY KEY,
#             empname text NOT NULL,
#             salary integer NOT NULL,
#             job text NOT NULL
#             );''')
# val = [
#  ("1", "john", "45000", "retail"),
#  ("2", "dave", "45000", "retail"),
#  ("3", "bobby", "95000", "retail"),
#  ("4", "rob", "85000", "retail"),
#  ("5", "roberta", "102000", "programmer")
# ]
# c.executemany('insert into EMP(empno,empname,salary,job) values(?,?,?,?);',val)
# conn.commit()
# print("table created successfully")
# conn.execute('INSERT INTO phonebook (phone_no,name,addr,social_media)\
#     VALUES ("4152780111", "Andy", "3221 drew cres.", "@andy")')
# conn.commit()
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json') #get request
data = response.json()
btccost = data["bpi"]["USD"]["rate"]

cmc = requests.get('https://production.api.coindesk.com/v1/currency/ticker?currencies=eth') #get request
soup = BeautifulSoup(cmc.content, 'html.parser')
json_object = json.loads(soup.contents[0])

ethcost = (json_object['data']['currency']['ETH']['quotes']['USD']['price'])

@app.route('/')
def index():
    return render_template('index.html', btccost=btccost, ethcost=ethcost)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST': #post request
        try:
            userform = request.form['username']
            passform = request.form['password']
            uid = 0
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("select uid from users where username=? AND password=?", (userform,passform))
                row = cur.fetchone()
                uid = row[0] + 1
                cur.execute("select username from users where username=? AND password=?", (userform,passform))
                user = cur.fetchone()
                username = user[0] + 1
            
                con.commit()
            print(uid, file=sys.stderr)
            if uid == '0':
                msg="Success!"
            else:
                msg="Login Failed"
        except:
            con.rollback()
            msg = "database error"
        finally:
            return render_template("dashboard.html", username=userform, uid=uid)
            con.close()
    if request.method == 'GET':
        return render_template("nologin.html") #get request

@app.route('/dashboard', methods = ['POST', 'GET'])#get request
def dashboard():
    if request.method == 'GET':
        return render_template('nologin.html')
    return render_template('dashboard.html')

@app.route('/games')
def games():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from game")
    games = cur.fetchall()

    return render_template("games.html", games=games)

@app.route('/newlist')
def newlist():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from game")
    games = cur.fetchall()
    return render_template('newlist.html', games=games)

@app.route('/nologin')
def nologin():
    return render_template('nologin.html')

@app.route('/postregister', methods = ['POST', 'GET'])
def postregister():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['pass']
            email = request.form['email']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                
            cur.execute("INSERT INTO 'users' (username,password,email)\
               VALUES (?,?,?)",(username,password,email) )
            con.commit()

            msg = "records added"
        except:
            con.rollback()
            msg = "An error has occured"
        
        finally:
            return render_template("result.html",msg = msg)
            con.close()
    
@app.route('/postphone', methods = ['POST', 'GET'])
def postphone():
    if request.method == 'POST':
        try:
            phone_no = request.form['phone_no']
            name = request.form['name']
            addr = request.form['addr']
            social_media = request.form['social_media']

            with sql.connect("database.db") as con:
                cur = con.cursor()

            cur.execute("INSERT INTO phonebook (phone_no,name,addr,social_media)\
               VALUES (?,?,?,?)",(phone_no,name,addr,social_media) )

            con.commit()
            msg = "records added"
        except:
            con.rollback()
            msg = "An error has occured"
        
        finally:
            return render_template("result.html",msg = msg)
            con.close()

@app.route('/newwallet')
def newwallet():
    return render_template('newwallet.html')

@app.route('/createwallet', methods = ['POST', 'GET'])
def createwallet():
    if request.method == 'POST':
        try:
            userform = request.form['username']
            passform = request.form['password']
            cryptotype = request.form['cryptotype']
            
            with sql.connect("database.db") as con:
                cur = con.cursor()
            balance=0
            cur.execute("select uid from users where username=? AND password=?", (userform,passform))
            row = cur.fetchone()
            uid = row[0] + 1
            cur.execute("INSERT INTO wallet (cryptotype,balance,uid) VALUES (?,?,?)",(cryptotype,balance,uid) )
            msg = "Wallet Added"
            con.commit()
        except:
            con.rollback()
            msg = "An error has occured, Please check user/pass and try again"
        
        finally:
            return render_template("result.html",msg = msg)
            con.close()

@app.route('/register')
def register():
    return render_template("register.html")
    con.close()

@app.route('/balance')
def balance():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    uid = request.args.get('uid')
    print(uid, file=sys.stderr)
    cur = con.cursor()
    
    cur.execute('select * from wallet where uid=?', (uid,))
    rows = cur.fetchall()
    balance = cur.fetchone()

    return render_template("balance.html", rows = rows, uid = uid)
    con.close()

@app.route('/addfunds', methods = ['POST', 'GET'])
def addfunds():
    if request.method =='POST':
        try:
            # response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json') #get request
            # data = response.json()
            # btccost = data["bpi"]["USD"]["rate"]
            cmc = requests.get('https://production.api.coindesk.com/v1/currency/ticker?currencies=btc') #get request
            soup = BeautifulSoup(cmc.content, 'html.parser')
            json_object = json.loads(soup.contents[0])

            btccost = (json_object['data']['currency']['BTC']['quotes']['USD']['price'])


            cmc = requests.get('https://production.api.coindesk.com/v1/currency/ticker?currencies=eth') #get request
            soup = BeautifulSoup(cmc.content, 'html.parser')
            json_object = json.loads(soup.contents[0])

            ethcost = (json_object['data']['currency']['ETH']['quotes']['USD']['price'])
            wid = request.form.get("wallet")
            con = sql.connect("database.db")
            con.row_factory = sql.Row

            with sql.connect("database.db") as con:
                cur = con.cursor()

            
            cur = con.cursor()
            print(wid, file=sys.stderr)
            cur.execute("select * from wallet where wid=?", (wid))
            rows = cur.fetchone()
            cur.execute("select balance from wallet where wid=?", (wid))
            balance = cur.fetchone()
            print(rows[1], balance[0], file=sys.stderr)
            
            ethbalance, btcbalance = (float(balance[0])/float(ethcost)), float(balance[0])/float(btccost)
            
            if rows[1] == 'BTC':
                balance = btcbalance
            if rows[1] == 'ETH':
                balance = ethbalance


            print(rows[1], balance[0], file=sys.stderr)
        except:
            con.rollback()
            msg = "An error has occured, Please check user/pass and try again"
        finally:
            return render_template("addfunds.html", wid=wid, rows=rows, ethcost=ethcost, btccost=btccost, balance=balance)
            con.close()

@app.route('/fundspost', methods = ['POST', 'GET'])
def fundspost():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    wid = request.args.get('staticwallet')
    amount = request.args.get('amount')

    cur = con.cursor()
    print(wid, amount, file=sys.stderr)
    cur.execute("select * from wallet where wid=?", (wid,))
    prebal = cur.fetchone()[2]
    newbal = int(prebal) + int(amount)
    cur.execute("select uid from wallet where wid=?", (wid,))
    uid = cur.fetchone()[0]
    cur.execute("update wallet set balance = ? where wid=?", (newbal,wid))
    con.commit()
    return render_template("dashboard.html", uid=uid, amount = amount)
    con.close()

@app.route('/addlist', methods = ['POST', 'GET'])
def addlist():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()

    username = request.form['username']
    wid = request.form['walletid']
    amount = request.form['amount']
    listing = request.form['listing']
    gamename = request.form.get("game")


    cur.execute("select * from wallet where wid=?", (wid))
    rows = cur.fetchone()

    print(gamename, file=sys.stderr)

    # print(wid, amount, file=sys.stderr)
    cur.execute("select * from wallet where wid=?", (wid,))
    prebal = cur.fetchone()[2]
    newbal = int(prebal) - int(amount)
    print(newbal, file=sys.stderr)
    cur.execute("select uid from wallet where wid=?", (wid,))
    uid = cur.fetchone()[0]
    cur.execute("update wallet set balance = ? where wid=?", (newbal,wid))

    cur.execute("select gid from game where name=?", (gamename,))
    gid = cur.fetchone()[0]

    cryptotype = rows[1]

    print(cryptotype, file=sys.stderr)
    cur.execute("INSERT INTO listing (name,username,price,cryptotype,gid) VALUES (?,?,?,?,?)",(listing,username,amount,cryptotype,gid) )




    con.commit()
    msg = "success"

    return render_template("result.html", msg=msg)
    con.close()


# for row in cursor:
#     print(row)
# conn.close()

if __name__ == "__main__":
    app.run(debug=True)