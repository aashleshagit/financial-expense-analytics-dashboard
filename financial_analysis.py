import pandas as pd

df = pd.read_excel(r"C:\Users\HP\OneDrive\Documents\expenses.xlsx")

income = df[df["Type"]=="Income"]["Amount"].sum()
expense = df[df["Type"]=="Expense"]["Amount"].sum()

savings = income - expense

print("Total Income:", income)
print("Total Expense:", expense)
print("Savings:", savings)

category_expense = df[df["Type"]=="Expense"].groupby("Category")["Amount"].sum()

print("\nExpense by Category:")
print(category_expense)