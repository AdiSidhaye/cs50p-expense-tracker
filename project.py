#importing the required libraries
from datetime import date
from hmac import new
from multiprocessing import Value
import tkinter as tk
from tkinter import messagebox,ttk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


#This is the main function for calling the other functions and generating the UI
def main():
    root=tk.Tk()
    root.title("Expense Tracker App")
    root.geometry("400*300")

    #labels and entries
    tk.Label(root, text="Expense:").grid(row=0, column=0, padx=10, pady=5)
    expense_entry = tk.Entry(root)
    expense_entry.grid(row=0, column=1)

    tk.Label(root, text="Amount:").grid(row=1, column=0, padx=10, pady=5)
    amount_entry = tk.Entry(root)
    amount_entry.grid(row=1, column=1)

    tk.Label(root, text="Category:").grid(row=2, column=0, padx=10, pady=5)
    categories = load_categories()
    category_cb = ttk.Combobox(root, values=categories, state='readonly')
    category_cb.grid(row=2, column=1)

    tk.Label(root, text="Date (DD-MM-YYYY):").grid(row=3, column=0, padx=10, pady=5)
    date_entry = tk.Entry(root)
    date_entry.grid(row=3, column=1)

    def load_categories():
        pass
    
    def submit_expense():
        expense=expense_entry.get()
        amount=amount_entry.get()
        category=category_cb.get()
        date=date_entry.get()
        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number")
            return
        CreateExp(expense, amount, category, date)

        tk.Button(root, text="Add Expense", command=submit_expense).grid(row=4, column=1, pady=20)

    root.mainloop()
        

#This is the function that actually create the database and adds to the database    
def CreateExp(expense, amount, category, date):
    # Create a DataFrame with the expense data
    try:
        newExpense = {
            'Expense': [expense],
            'Amount': [amount],
            'Category': [category],
            'Date': [date]
        }
        df = pd.DataFrame(newExpense,index=[1])

        output_path='data/expenses.csv'
        df.to_csv('data/expenses.csv', mode='a', header=not os.path.exists(output_path), index=False)
    #these are possible exceptions that can be raised,for now
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount")
        return
    except FileNotFoundError:
        messagebox.showerror("Error", "Database file not found")
        return
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        return
    

    
#This is the function to create new categories of expenses
def CreateNewCat():
    temp = input("Please enter the new category: ") 
    # Check if the category already exists
    df = pd.read_csv('data/categories.csv')
    for cat in df['Category'].values:
        if temp.lower()==cat.lower():
            messagebox.showerror("Error", "Category already exists")
            return
    # Add the new category to the DataFrame
    else:
        newCat={'Category':[temp]}
        df = pd.DataFrame(newCat)
        # Append the new category to the CSV file
        df.to_csv('data/categories.csv', mode='a', header=False, index=False)
        messagebox.showinfo("Success", "Category added successfully")   
        
        
        
    
#this is the function to create expense plots from given data/ pre existing data
def CreatePlot():
    ...


    