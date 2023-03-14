from flask import Flask, render_template, jsonify

app = Flask(__name__)

EXPERIENCES = [
  {
    'id': 1845,
    'company': 'Deloitte',
    'headquarters': 'London, United Kingdom',
    'revenue': '$59.3 Billion'
  },
  {
    'id': 1886,
    'company': 'Johnson & Johnson',
    'headquarters': 'New Jersey, USA',
    'revenue': '$94.94 Billion'
  },
  {
    'id': 1954,
    'company': 'City National Bank',
    'headquarters': 'Los Angeles, USA'
  },
  {
    'id': 2004,
    'company': 'Meta',
    'headquarters': 'Menlo Park, USA',
    'revenue': '$85.96 Billion'
  }
  ,
  {
    'id': 2000,
    'company': 'Thales',
    'headquarters': 'Paris, France',
    'revenue': '€16.19 Billion'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', exps=EXPERIENCES, name='Mohsen Dehhaghi')

@app.route("/api/experiences")
def list_experiences():
  return jsonify(EXPERIENCES)

# print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)