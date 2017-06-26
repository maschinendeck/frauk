import sqlite3, os
from flask import Flask, request, g, render_template, make_response, url_for
from flask_bootstrap import Bootstrap
from forms import AddDrink

app = Flask(__name__)
Bootstrap(app)
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

@app.route('/', methods = ['GET'])
def list_routes():
""" lists all routes that exist in this app """
    def has_no_empty_params(rule):
        defaults = rule.defaults if rule.defaults is not None else ()
        arguments = rule.arguments if rule.arguments is not None else ()
        return len(defaults) >= len(arguments)

    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    # links is now a list of url, endpoint tuples
    from flask import render_template_string
    tmpl="""
    <html>
        <head><title>list of endpoints for debugging</title></head>
        <body><h1>frauk</h1><h2>list of endpoints</h2>
        <ul>
        {% for route in routes %}
            <li>
            <a href="{{route[0]}}">{{route[1]}} ({{route[0]}})</a>
            </li>
        {% endfor %}
        </ul>
    </html>
    """
    return render_template_string(tmpl, routes=links)
    


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
            INSERT INTO drinks
            (name, bottle_size, caffeine, price,
            logo_file_name, created_at, updated_at,
            logo_content_type, logo_file_size,
            logo_updated_at, active)
            VALUES
            (:name, :bottle_size, :caffeine, :price,
            :logo_file_name, :created_at, :updated_at,
            :logo_content_type, :logo_file_size,
            :logo_updated_at, :active)
            ''', drink)
        db.commit()
        return 'hello ' + form.name.data
    return render_template('add_drink.html', form=form)


if __name__ == '__main__':
    app.run()
