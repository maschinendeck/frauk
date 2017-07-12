from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for
from werkzeug.utils import secure_filename
import os
    

from app.model import User, Drink, Audit
from app.forms import AddUser, AddDrink
from app import app, db


@app.route("/")
def site_map():
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





