from flask import Flask, jsonify, Response 
from flask import jsonify
import sys
from flask import jsonify
import json
from flask import json

app = Flask(__name__)

@app.route('/date/<ageInMonths>', methods=['GET', 'POST'])
def prime(ageInMonths):
    try:
        ageMonths = int(float(ageInMonths))
    except ValueError:
        return "ValueError: please enter a number"
    if ageMonths > 1:
        if ageMonths % 2 == 1 or ageMonths == 2:
            prime = "yes, you are PRIME"
        elif ageMonths % 2 == 0:
            prime = "No, you are COMPOSITE"
    elif ageMonths == 1:
            prime = "neither PRIME nor COMPOSITE"
    else:
        prime = "You do not appear to exist"
    print(str(prime), file=sys.stderr)
    print(str(prime), file=sys.stdout)
    return prime