from setuptools import setup

setup(
    name="frauk",
    version="0.0.1",
    packages=['frauk'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask_sqlalchemy==2.1',
        'flask_wtf',
        'flask_bootstrap',
        'fnvhash',
        'pillow'
    ]
)
