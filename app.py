from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask(__name__)

with open('config.json') as f:
        config_json = json.load(f)
        
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{}:{}@{}/{}'.format(config_json['username'], config_json['password'], config_json['hostname'], config_json['database'])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False 

db = SQLAlchemy(app)

# Defined users table model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

# before_first_request decorated is deprecated
# @app.before_first_request
# def createTable():
#     db.create_all()
    
# @app.before_request
# def createTable():
#     app.before_request_funcs[none].remove(create_tables)
#     db.create_all()

with app.app_context():
    db.create_all()
    
#Default route    
@app.route('/',methods=['GET'])
def createUser1():
    data = "Hello World"
    return f"<h1>{data}</h1>", 200

#POST call
@app.route('/users',methods=['POST'])
def createUser():
    data = request.get_json()
    new_user = Users(name = data['name'], role = data['role'], email = data['email'])
    db.session.add(new_user)
    db.session.commit()
    
    userData = {
        'id': new_user.id,
        'name': new_user.name,
        'role': new_user.role,
        'email': new_user.email
    }
    return jsonify({'message': 'User created successfully','user': userData}), 200

# GET call
@app.route('/users', methods=['GET'])
def getUsers():
    users = Users.query.all()
    # Get users get based on ID
    # user = Users.query.get_or_404(id)
    return jsonify([{'id':user.id,'name':user.name,'role':user.role,'email':user.email} for user in users]), 200

# PUT call
@app.route("/users/<int:id>", methods=['PUT'])
def updateUser(id):
    user = Users.query.get_or_404(id)
    data = request.get_json()

    user.name = data.get('name', user.name)
    user.role = data['role']
    user.email = data['email']

    db.session.commit()

    updatedUser = {
        'id': user.id,
        'name': user.name,
        'role': user.role,
        'email': user.email
    }

    return jsonify({"message": "User updated successfully", "updated_user": updatedUser}), 200

#DELETE call  
@app.route('/users/<int:id>', methods=['DELETE'])
def deleteUser(id):
    user = Users.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}),200

# Setting Port to localhost:5000
# if __name__ == "__main__":
#     app.run()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
