import sys

SALARY_PER_HOUR = 6.50
SALARY_PER_MINUTE_NORMAL_SCHEDULE = 6.50 / 60
SALARY_PER_MINUTE_EXTRA_SCHEDULE = SALARY_PER_MINUTE_NORMAL_SCHEDULE + SALARY_PER_MINUTE_NORMAL_SCHEDULE / 2

HOUR_START = 18
MINUTE_START = 0

def get_salary(salary, hour, minute):
    normal_hours_worked = hour - HOUR_START
    normal_minutes_worked = (minute - MINUTE_START)
    
    
    

def test_get_salary():
    for line in sys.stdin:
        line_splitted = line.split(" ")
        try:
            salary = float(line_splitted[0])
            hour = int(line_splitted[1])
            minute = int(line_splitted[2]) 
        except Exception:
            sys.exit(0)
        
        if hour < 0 or minute < 0 or salary < 0 or hour > 24 or minute > 60:
            sys.exit(0)
        
        sal = get_salary(salary, hour, minute)
        
        
        
def main():
    test_get_salary()

if __name__ == "__main__":
    main()