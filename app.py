from flask import Flask, render_template, jsonify, url_for
from database import load_roles_from_db, load_role_from_db



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

  
# Load Browser Favorite Icon
@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='favicon.ico')

# print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)