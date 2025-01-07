# A- Discounts and Pricing

# 1. Check Discount Eligibility
total_purchase = float(input("Enter the total purchase amount: "))
if total_purchase > 100:
    final_price = total_purchase * 0.9
else:
    final_price = total_purchase
print(f"Final price: ${final_price:.2f}")

# 2. Calculate Bulk Discount
num_items = int(input("Enter the number of items: "))
total_price = float(input("Enter the total price: "))
if num_items > 5:
    final_price = total_price * 0.85
else:
    final_price = total_price
print(f"Final price: ${final_price:.2f}")

# 3. Membership Discount
is_member = input("Are you a member? (yes/no): ").strip().lower() == "yes"
total_price = float(input("Enter the total price: "))
if is_member:
    final_price = total_price * 0.8
else:
    final_price = total_price * 0.95
print(f"Discounted price: ${final_price:.2f}")

# 4. Seasonal Sale
is_holiday = input("Is today a holiday? (yes/no): ").strip().lower() == "yes"
total_price = float(input("Enter the total price: "))
if is_holiday:
    final_price = total_price * 0.75
else:
    final_price = total_price * 0.9
print(f"Price after discount: ${final_price:.2f}")

# 5. Buy-One-Get-One-Free
num_items = int(input("Enter the number of items: "))
pay_for = num_items // 2 + num_items % 2
print(f"Number of items to pay for: {pay_for}")

# B- Tax Calculations

# 6. Sales Tax
price = float(input("Enter the price of the item: "))
if price > 500:
    total_price = price * 1.15
else:
    total_price = price * 1.08
print(f"Total price after tax: ${total_price:.2f}")

# 7. Income Tax
income = float(input("Enter your annual income: "))
if income > 50000:
    tax = income * 0.2
else:
    tax = income * 0.1
print(f"Tax amount: ${tax:.2f}")

# 8. Tax Bracket
income = float(input("Enter your annual income: "))
if income < 30000:
    bracket = "Low Tax"
elif income < 100000:
    bracket = "Medium Tax"
else:
    bracket = "High Tax"
print(f"Tax bracket: {bracket}")

# 9. VAT Calculation
is_essential = input("Is the item essential? (yes/no): ").strip().lower() == "yes"
price = float(input("Enter the price of the item: "))
if is_essential:
    final_price = price * 1.05
else:
    final_price = price * 1.12
print(f"Final price: ${final_price:.2f}")

# 10. Tax-Free Day
tax_free = input("Is today a tax-free day? (yes/no): ").strip().lower() == "yes"
price = float(input("Enter the price of the item: "))
if tax_free:
    final_price = price
else:
    final_price = price * 1.07
print(f"Final price: ${final_price:.2f}")

# C- Shopping and Billing

# 11. Free Shipping
total_purchase = float(input("Enter the total purchase amount: "))
if total_purchase > 50:
    shipping_cost = 0
else:
    shipping_cost = 5
final_price = total_purchase + shipping_cost
print(f"Total amount including shipping: ${final_price:.2f}")

# 12. Discount Code
total_price = float(input("Enter the total price: "))
discount_code = input("Enter the discount code: ").strip()
if discount_code == "DISCOUNT10":
    final_price = total_price * 0.9
else:
    final_price = total_price
print(f"Final price: ${final_price:.2f}")

# 13. Tiered Discounts
total_price = float(input("Enter the total price: "))
if total_price <= 50:
    discount = 0
elif total_price <= 100:
    discount = 0.1
else:
    discount = 0.2
final_price = total_price * (1 - discount)
print(f"Final price: ${final_price:.2f}")

# 14. Minimum Purchase Requirement
total_price = float(input("Enter the total amount: "))
if total_price < 20:
    print("Minimum purchase of $20 is required.")
else:
    print(f"Total amount: ${total_price:.2f}")

# 15. Loyalty Points
total_purchase = float(input("Enter the total purchase amount: "))
is_loyal = input("Are you a loyal member? (yes/no): ").strip().lower() == "yes"
if is_loyal:
    points = total_purchase * 2
else:
    points = total_purchase
print(f"Loyalty points earned: {points}")

# D- Travel and Tickets

# 16. Travel Discount
distance = float(input("Enter the travel distance in miles: "))
ticket_price = float(input("Enter the ticket price: "))
if distance > 500:
    final_price = ticket_price * 0.8
else:
    final_price = ticket_price
print(f"Final ticket price: ${final_price:.2f}")

# 17. Child or Senior Discount
age = int(input("Enter the passenger's age: "))
ticket_price = float(input("Enter the ticket price: "))
if age < 12 or age > 60:
    final_price = ticket_price * 0.85
else:
    final_price = ticket_price
print(f"Final ticket price: ${final_price:.2f}")

# 18. Ticket Type Pricing
is_weekend = input("Is the ticket for a weekend? (yes/no): ").strip().lower() == "yes"
ticket_price = float(input("Enter the ticket price: "))
if is_weekend:
    final_price = ticket_price * 1.1
else:
    final_price = ticket_price
print(f"Final ticket price: ${final_price:.2f}")

# 19. Baggage Fee
baggage_weight = float(input("Enter the total baggage weight in kg: "))
if baggage_weight > 20:
    extra_fee = (baggage_weight - 20) * 10
else:
    extra_fee = 0
print(f"Extra baggage fee: ${extra_fee:.2f}")

# 20. Early Bird Discount
days_in_advance = int(input("Enter the number of days before travel: "))
ticket_price = float(input("Enter the ticket price: "))
if days_in_advance > 30:
    final_price = ticket_price * 0.9
else:
    final_price = ticket_price
print(f"Final ticket price: ${final_price:.2f}")

# E- Grades and Performance

# 21. Pass or Fail
score = float(input("Enter the student's score: "))
if score >= 40:
    print("Pass")
else:
    print("Fail")

# 22. Grade Assignment
score = float(input("Enter the student's score: "))
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "F"
print(f"Grade: {grade}")

# 23. Bonus Marks
score = float(input("Enter the student's score: "))
completed_assignments = input("Has the student completed all assignments? (yes/no): ").strip().lower() == "yes"
if completed_assignments:
    score += 5
print(f"Final score: {score}")

# 24. Attendance Eligibility
attendance = float(input("Enter the student's attendance percentage: "))
if attendance >= 75:
    print("Eligible to take the exam.")
else:
    print("Not eligible to take the exam.")

# 25. Scholarship Eligibility
grade = input("Enter the student's grade: ").strip().upper()
family_income = float(input("Enter the annual family income: "))
if grade == "A" and family_income < 30000:
    print("Eligible for a scholarship.")
else:
    print("Not eligible for a scholarship.")
