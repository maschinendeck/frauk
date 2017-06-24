DROP TABLE IF EXISTS audits;
CREATE TABLE audits (
    id integer primary key autoincrement,
    created_at text not null,
    difference real not null,
    drink integer not null,
    user integer not null
);

DROP TABLE IF EXISTS drinks;
CREATE TABLE drinks (
    id integer primary key autoincrement,
    bottle_size real not null,
    caffeine integer not null,
    price real not null,
    logo_file_name text,
    created_at text not null,
    updated_at text not null,
    logo_content_type text not null,
    logo_file_size integer not null,
    logo_updated_at text not null,
    active integer not null
);

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id integer primary key autoincrement,
    name text not null,
    email text not null,
    created_at text not null,
    updated_at text not null,
    balance real not null,
    active integer not null,
    audit integer not null,
    redirect integer not null
);
