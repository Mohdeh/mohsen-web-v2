from flask import Flask, render_template, jsonify, url_for, request
from database import load_roles_from_db, load_role_from_db, add_inquiry_to_db


app = Flask(__name__)


@app.route("/")
def hello_world():
  roles = load_roles_from_db()
  return render_template('home.html', 
                         roles=roles, 
                         name='Mohsen Dehhaghi')

@app.route("/api/roles")
def list_roles():
  roles = load_roles_from_db()
  return jsonify(roles)


@app.route("/role/<id>")
def show_role(id):
  role = load_role_from_db(id)
  if not role:
    return "Not Found", 404
  return render_template('rolepage.html', role=role, name='Mohsen Dehhaghi')


@app.route("/api/role/<id>")
def show_role_json(id):
  role = load_role_from_db(id)
  return jsonify(role)

@app.route("/role/<id>/inquiry", methods=['post'])
def inquiry_about_role(id):
  # data = request.args
  data = request.form
  role = load_role_from_db(id) # display and acknowledgement
  
  add_inquiry_to_db(id, data) # store data in DB
  
  # send an email
  

  return render_template('inquiry.html', inquiry=data, name='Mohsen Dehhaghi',
                        role=role)
  # return jsonify(data)


# Load Browser Favorite Icon
@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='favicon.ico')

# print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)