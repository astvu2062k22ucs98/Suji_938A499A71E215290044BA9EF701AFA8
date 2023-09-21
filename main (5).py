def calculate_cgpa_and_percentage(marks): # Assuming that marks are out of 100
  n = len(marks)
  cgpa=sum (marks)/(n*10)
  cgpa_percentage = cgpa * 9.5 * 10
  return cgpa,cgpa_percentage

# Driver code

n = 5

marks = [90, 80, 70, 80, 90]

cgpa, cgpa_percentage = calculate_cgpa_and_percentage(marks)
 
print("CGPA =",'%.1f'% cgpa)

print("CGPA Percentage = ",'%.2f'%

cgpa_percentage)