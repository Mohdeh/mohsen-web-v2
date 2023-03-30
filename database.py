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


  
  

