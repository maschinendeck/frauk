import sqlite3, os
from flask import Flask, request, g, render_template, make_response
from forms import AddDrink

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update({
    'DATABASE'      : os.path.join(app.root_path, 'dev.db'),
    'SECRET_KEY'    : 'devkey',
    'USERNAME'      : 'admin',
    'PASSWORD'      : 'default'
    })
app.config.from_envvar('PLUGIN_REPO_SETTINGS', silent=True)


def dict_factory(cursor, row):
    """Function to turn DB queries into dicts"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = dict_factory
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/add_drink', methods = ['GET','POST'])
def add_drink():
    form = AddDrink()
    if form.validate_on_submit():
        print "test"
        drink = {
            "name" : form.name.data,
            "bottle_size" : form.bottle_size.data,
            "caffeine" : form.caffeine.data,
            "price" : form.price.data,
            "logo_file_name" : form.logo_file_name.data,
            "created_at" : 'tbd',
           "updated_at" : 'tbd',
            "caffeine" : form.caffeine.data,
            "logo_content_type" : 'tbd',
            "logo_file_size" : 'tbd',
            "logo_updated_at" : 'tbd',
            "active" : 1}
        db = get_db()
        cur = db.execute('''
            INSER INTO drinks
            (name, bottle_size, caffeine, price,
            logo_file_name, created_at, updated_at,
            logo_content_type, logo_file_size,
            logo_updated_at, active)
            (:name, :bottle_size, :caffeine, :price,
            :logo_file_name, :created_at, :updated_at,
            :logo_content_type, :logo_file_size,
            :logo_updated_at, :active)
            ''', drink)
        return 'hello ' + form.name.data
    return render_template('add_drink.html', form=form)


if __name__ == '__main__':
    app.run()
