from employee import employee_details


def test_employee_details_output():
    result = employee_details("ananya", "E190", "Accounts", 100000)

    expected = (
        "Employee Name: ananya\n"
        "Employee ID: E190\n"
        "Employee Department: Accounts\n"
        "Employee Salary: 100000"
    )

    assert result == expected
