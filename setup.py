from setuptools import setup

setup(
    name="frauk",
    version="0.0.1",
    packages=['app'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'flask_wtf',
        'flask_bootstrap'
    ]
)
