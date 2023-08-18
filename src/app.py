from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (can be replaced with a database)
employees = [
    {'id': 1, 'name': 'Ratnam', 'email': 'ratnam@contoso.com', 'department': 'IT'},
    {'id': 2, 'name': 'Martin', 'email': 'martin@contoso.com','department': 'IT'}
]

# Get all the employees information
@app.route('/employees', methods=['GET'])
def get_all_employees():
    return jsonify(employees)

# Add a new employee information
@app.route('/employees', methods=['POST'])
def add_employees():
    new_employee={'id':request.json['id'], 'name':request.json['name'], 'email':request.json['email'], 'department':request.json['department']}
    employees.append(new_employee)
    return jsonify(new_employee)

# Update the existing employee information
@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    for employee in employees:
        if employee['id']==employee_id:
            employee['name']=request.json['name']
            employee['email']=request.json['email']
            employee['department']=request.json['department']
            return jsonify(employee)
    return jsonify({'error':'Employee not found'})

# Delete the existing employee information
@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    for employee in employees:
        if employee['id']==employee_id:
            employees.remove(employee)
            return jsonify({"Message":"The employee information is deleted successfully"})

    return jsonify({'error':'Employee not found'})

@app.route('/health', methods=['GET'])
def app_health():
    return jsonify({"Message":"The application is running smoothly"})

# Run the flask App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5001,debug=True)