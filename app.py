from flask import Flask, request, jsonify
from operator import itemgetter

app = Flask(__name__)

# Sample employee data (you can replace this with a database)
employees = [
    {"id": 1, "name": "John Doe", "department": "Engineering"},
    {"id": 2, "name": "Jane Smith", "department": "HR"},
    {"id": 3, "name": "Alice Johnson", "department": "Finance"},
    {"id": 4, "name": "Bob Williams", "department": "Marketing"},
    {"id": 5, "name": "Emily Brown", "department": "Sales"},
    {"id": 6, "name": "Michael Jones", "department": "Engineering"},
    {"id": 7, "name": "Sarah Davis", "department": "HR"},
    {"id": 8, "name": "William Wilson", "department": "Finance"},
    {"id": 9, "name": "Laura Taylor", "department": "Marketing"},
    {"id": 10, "name": "James Miller", "department": "Sales"},
    {"id": 11, "name": "Linda Moore", "department": "Engineering"},
    {"id": 12, "name": "David Garcia", "department": "HR"},
    {"id": 13, "name": "Mary Clark", "department": "Finance"},
    {"id": 14, "name": "Richard Rodriguez", "department": "Marketing"},
    {"id": 15, "name": "Patricia Hernandez", "department": "Sales"}
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

@app.route('/employees/count', methods=['GET'])
def get_employee_count():
    return jsonify({"count": len(employees)})

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

@app.route('/sort_employees', methods=['GET'])
def get_employees_sorted():
    department = request.args.get('department')
    sort_by = request.args.get('sort_by')
    order = request.args.get('order')

    filtered_employees = employees
    if department:
        filtered_employees = [employee for employee in employees if employee["department"] == department]

    if sort_by:
        if order == 'ASC':
            filtered_employees = sorted(filtered_employees, key=itemgetter(sort_by.lower()))
        elif order == 'DESC':
            filtered_employees = sorted(filtered_employees, key=itemgetter(sort_by.lower()), reverse=True)

    return jsonify(filtered_employees)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
