# Employee Management API

This is a simple RESTful API built using Python's Flask framework to manage employee data. The API provides endpoints for performing CRUD operations (Create, Read, Update, Delete) on employee records.

## Features
GET - Retrieve all employees or a specific employee by ID
POST - Add a new employee
PUT - Update an existing employee by ID
DELETE - Delete an employee by ID

### Prerequisites
Python 3.x
Flask
requests

### Setup and Installation

Clone the repository
```shell 
git clone https://github.com/yourusername/employee-management-api.git
``` 

### Install dependencies

```shell
pip install Flask requests

OR

poetry install

OR 

./001.bat

```

### Run the application

```shell
python app.py

OR
poetry run python app.py

OR

./002.bat

```

```shell
The application should now be running at http://127.0.0.1:5000/.
```

### API Endpoints

#### Retrieve All Employees
URL: /employees
Method: GET

Success Response:
Code: 200 OK
Content: JSON array of employee records

#### Retrieve a Specific Employee
URL: /employees/<employee_id>
Method: GET
Success Response:
Code: 200 OK
Content: JSON object of the specified employee
Error Response:
Code: 404 Not Found
Content: { "error": "Employee not found" }

#### Add a New Employee
URL: /employees
Method: POST
Data Params: { "name": "John Doe", "department": "Engineering" }
Success Response:
Code: 201 Created
Content: JSON object of the new employee

#### Update an Existing Employee
URL: /employees/<employee_id>
Method: PUT
Data Params: { "name": "John Doe Updated", "department": "Engineering" }
Success Response:
Code: 200 OK
Content: JSON object of the updated employee
Error Response:
Code: 404 Not Found
Content: { "error": "Employee not found" }

#### Delete an Employee
URL: /employees/<employee_id>
Method: DELETE
Success Response:
Code: 200 OK
Content: { "message": "Employee deleted" }
Error Response:
Code: 404 Not Found
Content: { "error": "Employee not found" }

### Testing the API
You can test the API using the requests library in Python or any API testing tool like Postman.

Here are some sample Python requests:

``` python
import requests

# GET All Employees
response = requests.get('http://127.0.0.1:5000/employees')
print(response.json())

# GET Single Employee
response = requests.get('http://127.0.0.1:5000/employees/1')
print(response.json())

# POST New Employee
new_employee = {"name": "Bob Smith", "department": "Marketing"}
response = requests.post('http://127.0.0.1:5000/employees', json=new_employee)
print(response.json())

# PUT (Update) Employee
updated_employee = {"name": "John Doe Updated", "department": "Engineering"}
response = requests.put('http://127.0.0.1:5000/employees/1', json=updated_employee)
print(response.json())

# DELETE Employee
response = requests.delete('http://127.0.0.1:5000/employees/1')
print(response.json())
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.