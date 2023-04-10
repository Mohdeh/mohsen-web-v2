from sqlalchemy import create_engine, text
# print("sqlalchemy version: ", sqlalchemy.__version__)
import os


db_connection_string = os.environ['MSN_DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                        connect_args={
                          "ssl": {
                              "ssl_ca": "/etc/ssl/cert.pem"
                          }
                        }
                      )


def load_roles_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from roles"))
  #  result_dict = [row._asdict() for row in result.all()]
    roles = []
    for row in result.all():
      roles.append(row._asdict())
    return roles


def load_role_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM roles WHERE id = {id}")
    )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()


def add_inquiry_to_db(role_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO inquiries (role_id, full_name, email, linkedin, education, work_experience, resume) VALUES (:role_id, :full_name, :email, :linkedin, :education, :work_experience, :resume)")

    conn.execute(query, {
                'role_id': role_id,
                'full_name': data['full_name'],
                'email': data['email'],
                'linkedin': data['linkedin'],
                'education': data['education'],
                'work_experience': data['work_experience'],
                'resume': data['resume']
    })
  

