#! /usr/bin/env python
# encoding: utf-8

from flask import Blueprint

qa = Blueprint('qa', __name__, url_prefix='')

@qa.route('/')
def index():
	return "<p>Hellw World</p>"