def main():
    grades = []
    
    print("Enter 10 grades (85.5, 90.6, 100, 75, 90.5, 80, 78, 90, 65,85):")
    
    for i in range(10):
        while True:
            try:
                grade = float(input(f"Grade {i + 1}: "))
                grades.append(grade)
                break
            except ValueError:
                print("Invalid input! Please enter a number (e.g., 88.5, 75.8, 100, 90.5).")
                
    total = sum(grades)
    average = total / len(grades)
    maximum = max(grades)
    minimum = min(grades)
    
    print("\nGrade Statistics:")
    print(f"Total of Grades: {total:.2f}")
    print(f"Average Grade: {average:.2f}")
    print(f"Highest Grade: {maximum:.2f}")
    print(f"Lowest Grade: {minimum:.2f}")
    
if __name__ == "__main__":
    main()