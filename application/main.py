from flask import Flask, request, render_template, redirect, url_for, session
import json
import datetime
import sqlite3

from algosdk.future import transaction
from algosdk import account, mnemonic, logic, encoding
from algosdk.v2client import algod

from pyteal import *

import hashlib
import re
from base64 import b64encode, b64decode

from Cryptodome.Cipher import AES
import os
from Cryptodome.Random import get_random_bytes

import random

import requests

app = Flask(__name__, static_url_path='/static')
app.secret_key = "cIl7PtYtOn3hm2uJKjyM"

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")