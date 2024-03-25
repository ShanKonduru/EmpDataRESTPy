import requests
import time

# Base URL of the API
BASE_URL = 'http://127.0.0.1:5000'

def test_get_employees():
    response = requests.get(f'{BASE_URL}/employees')
    
    # Check response status
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    # Check response time
    assert response.elapsed.total_seconds() < 1, "Response time is too high"
    
    # Check return value
    data = response.json()
    assert isinstance(data, list), "Expected a list of employees"
    assert len(data) == get_employee_count(), "Expected 5 employees"

def get_employee_count():
    response = requests.get(f'{BASE_URL}/employees/count')    
    # Check return value
    data = response.json()
    return data["count"]

def test_get_employee_count():
    response = requests.get(f'{BASE_URL}/employees/count')
    
    # Check response status
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    # Check response time
    assert response.elapsed.total_seconds() < 1, "Response time is too high"
    
    # Check return value
    data = response.json()
    assert isinstance(data, dict), "Expected a dictionary"
    assert "count" in data, "Expected 'count' key in response"
    assert data["count"] == get_employee_count(), "Expected count to be 5"


# Test POST New Employee
def test_add_employee():
    new_employee = {"name": "Test Employee", "department": "Test Department"}
    response = requests.post(f'{BASE_URL}/employees', json=new_employee)
    assert response.status_code == 201
    assert response.elapsed.total_seconds() < 1
    assert isinstance(response.json(), dict)

# Test PUT (Update) Employee
def test_update_employee():
    updated_employee = {"name": "Updated Test Employee", "department": "Updated Test Department"}
    response = requests.put(f'{BASE_URL}/employees/1', json=updated_employee)
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 1
    assert response.json()["name"] == "Updated Test Employee"
    assert response.json()["department"] == "Updated Test Department"

# Test DELETE Employee
def test_delete_employee():
    response = requests.delete(f'{BASE_URL}/employees/1')
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 1
    assert response.json()["message"] == "Employee deleted"

# Test Count of Employees
def test_count_employees():
    response = requests.get(f'{BASE_URL}/employees')
    employee_count = len(response.json())
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 1
    assert employee_count == get_employee_count()  # Assuming one employee was deleted in the previous test

# Test GET Single Employee
def test_get_employee():
    response = requests.get(f'{BASE_URL}/employees/1')
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 1
    assert isinstance(response.json(), dict)

if __name__ == '__main__':
    test_get_employees()
    test_get_employee_count()
    test_get_employee()
    test_add_employee()
    test_update_employee()
    test_delete_employee()
    test_count_employees()
    print("All tests passed!")