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
from backend import db
from backend.user.model import User
from backend.product.model import Product
from backend.audit.model import Audit

db.create_all()

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
    user.name = row[1]
    user.email = row[2]
    user.created_at = datetime.datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S.%f")
    user.updated_at = datetime.datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S.%f")
    user.balance = int(row[5] * 100)
    user.active = row[6]
    user.audit = (row[7] == 't')
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
    product = Product()
    product.id = row[0]
    product.name = row[1]
    product.bottle_size_l = row[2]
    product.caffeine_mg = row[3]
    product.price = int(row[4] * 100)
    product.created_at = datetime.datetime.strptime(row[6], "%Y-%m-%d %H:%M:%S.%f")
    product.updated_at = datetime.datetime.strptime(row[7], "%Y-%m-%d %H:%M:%S.%f")
    db.session.add(product)
db.session.commit()

res = cur.execute('''
    SELECT
    id, created_at, difference, drink, user from audits;
''')
rows = res.fetchall()

for row in rows:
    audit = Audit()
    uid = row[4]
    if not uid: uid = 0
    audit.id = row[0]
    audit.created_at = datetime.datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S.%f")
    audit.difference = row[2] * 100
    audit.product_id = row[3]
    audit.user_id = uid
    db.session.add(audit)


db.session.commit()

