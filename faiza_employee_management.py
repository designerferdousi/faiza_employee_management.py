# Get employee information
def get_employee_details():
  name = input("Enter Employee name: ")
  employee_id = input("Enter Employee ID: ")
  salary = input("Enter Salary: ")
  return name, employee_id, salary

# Add employee information to the file
def add_employee(name, employee_id, salary):
  with open("employees.txt", "a") as file:
    file.write(f"{name} | {employee_id} | {salary}\n")
    print("Employee Added Successfully!")

# View all employee records
def view_employees():
    try:
      with open("employees.txt","r") as file:
       records = file.readlines()
      if len(records) == 0:
        print("No Employee records Found.")
      else:
        print("\nEmployee Records: ")
        for record in records:
          print(record.strip())
    except FileNotFoundError:
      print("No Employee Records Found.")

# Main menu
def main():
  while True:
    print("\n1.Add Employee ")
    print("2.View Employees ")
    print("3.Exit")

    choice = input("Choose Option: ")
    if choice == "1":
      name, employee_id, salary = get_employee_details()
      add_employee(name, employee_id, salary)
    elif choice == "2":
      view_employees()
    elif choice == "3":
      print("Exiting Program...")
      break
    else:
      print("Invalid Option! Try Again.")
main()
