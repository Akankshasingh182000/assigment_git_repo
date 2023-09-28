# Function to parse the time string and convert it to minutes
def parse_time(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

# Function to check if an employee meets the criteria
def check_employee(employee):
    consecutive_days = 0
    last_shift_end_time = None

    for record in employee['records']:
        shift_start_time = parse_time(record['start_time'])
        shift_end_time = parse_time(record['end_time'])
        
        if last_shift_end_time is not None:
            time_between_shifts = shift_start_time - last_shift_end_time
            if 60 < time_between_shifts < 600:  # Between 1 hour and 10 hours
                print(f"Employee {employee['name']} ({employee['position']}) has less than 10 hours between shifts.")
        
        if shift_end_time - shift_start_time > 840:  # More than 14 hours in a single shift
            print(f"Employee {employee['name']} ({employee['position']}) worked for more than 14 hours in a single shift.")

        last_shift_end_time = shift_end_time
        consecutive_days += 1

        if consecutive_days == 7:
            print(f"Employee {employee['name']} ({employee['position']}) has worked for 7 consecutive days.")
            break

# Main function
def main(filename):
    with open(filename, 'r') as file:
        employees = []
        current_employee = None

        for line in file:
            parts = line.strip().split(',')
            
            if len(parts) == 3:
                if current_employee:
                    employees.append(current_employee)
                current_employee = {'name': parts[0], 'position': parts[1], 'records': []}
            elif len(parts) == 2:
                record = {'start_time': parts[0], 'end_time': parts[1]}
                current_employee['records'].append(record)

        if current_employee:
            employees.append(current_employee)

        for employee in employees:
            check_employee(employee)

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    main(filename)
