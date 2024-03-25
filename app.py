from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample employee data (you can replace this with a database)
employees = [
    {"id": 1, "name": "John Doe", "department": "Engineering"},
    {"id": 2, "name": "Jane Smith", "department": "HR"},
    {"id": 3, "name": "Alice Johnson", "department": "Finance"},
]

# Helper function to find an employee by ID
def find_employee_by_id(employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return None

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = find_employee_by_id(employee_id)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({"error": "Employee not found"}), 404

@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    new_employee = {
        "id": len(employees) + 1,
        "name": data["name"],
        "department": data["department"]
    }
    employees.append(new_employee)
    return jsonify(new_employee), 201

@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    employee = find_employee_by_id(employee_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    
    data = request.get_json()
    employee["name"] = data["name"]
    employee["department"] = data["department"]
    
    return jsonify(employee)

@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employee = find_employee_by_id(employee_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    
    employees.remove(employee)
    return jsonify({"message": "Employee deleted"})


if __name__ == '__main__':
    app.run(debug=True)