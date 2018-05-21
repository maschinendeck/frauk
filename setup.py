from setuptools import setup

setup(
    name="frauk",
    version="0.0.1",
    packages=['backend'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-cors',
        'graphene',
        'graphene-sqlalchemy',
        'marshmallow-sqlalchemy',
        'flask-graphql',
        'flask_sqlalchemy==2.1',
        'flask-marshmallow'
    ]
)
