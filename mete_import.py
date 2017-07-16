"""
Import script from mete to frauk

you need to delete the frauk database manually
then you need to call:

$ python mete_import.py /path/to/mete.db

and if the script does not explode, you should now have everything you need.
"""
import sqlite3
import sys
import datetime
from app import db, colors
from app.model import User, Drink, Audit

db.create_all()

#con = sqlite3.connect('/home/vann/projects/frauk/mete/mete.db')
con = sqlite3.connect(sys.argv[1])

cur = con.cursor()

res = cur.execute('''SELECT 
    id, 
    name, 
    email, 
    created_at, 
    updated_at, 
    balance, 
    active, 
    audit FROM users;''')

rows = res.fetchall()

for row in rows:
    user = User()
    user.id = row[0]
    user.username = row[1]
    user.email = row[2]
    user.created_at = datetime.datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S.%f")
    user.updated_at = datetime.datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S.%f")
    user.balance = row[5]
    user.active = row[6]
    user.audit = (row[7] == 't')
    user.color = colors.from_name(row[1])
    db.session.add(user)
db.session.commit()

res = cur.execute('''SELECT 
    id, 
    name, 
    bottle_size, 
    caffeine, 
    price, 
    logo_file_name, 
    created_at, 
    updated_at, 
    logo_content_type, 
    logo_file_size, 
    logo_updated_at FROM drinks;''')
rows = res.fetchall()

for row in rows:
    drink = Drink()
    drink.id = row[0]
    drink.name = row[1]
    drink.bottle_size_l = row[2]
    drink.caffeine_mg = row[3]
    drink.price = row[4]
    drink.color = colors.from_name(row[1])
    drink.created_at = datetime.datetime.strptime(row[6], "%Y-%m-%d %H:%M:%S.%f")
    drink.updated_at = datetime.datetime.strptime(row[7], "%Y-%m-%d %H:%M:%S.%f")
    db.session.add(drink)
db.session.commit()

res = cur.execute('''
    SELECT
    id, created_at, difference, drink, user from audits;
''')
rows = res.fetchall()

for row in rows:
    uid = row[4]
    if not uid: uid = 0
    audit = Audit(row[2], row[3], uid)
    audit.id = row[0]
    audit.created_at = datetime.datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S.%f")
    db.session.add(audit)


db.session.commit()

