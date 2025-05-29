#importing the required libraries
from datetime import datetime 
from hmac import new
from math import nan
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
    root.geometry("400x300")

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

    tk.Label(root, text="New Category:").grid(row=3, column=0, padx=10, pady=5)
    new_category_entry = tk.Entry(root)
    new_category_entry.grid(row=3, column=1) 

    tk.Label(root, text="Date (DD-MM-YYYY):").grid(row=4, column=0, padx=10, pady=5)
    date_entry = tk.Entry(root)
    date_entry.grid(row=4, column=1) 


        
    def submit_expense():
        expense=expense_entry.get()
        amount=amount_entry.get()
        category=category_cb.get()
        date=date_entry.get()

        try:
            parsed_date = datetime.strptime(date, "%d-%m-%Y").date()
            date = parsed_date.strftime('%d-%m-%Y')  # Optional; keeps format consistent
        except ValueError:
            messagebox.showerror("Error", "Date must be in DD-MM-YYYY format")
            return
                
        # try:
        #     amount = float(amount)
        # except ValueError:
        #     messagebox.showerror("Error", "Amount must be a number")
        #     return
        
        CreateExp(expense, amount, category, date)

    def submit_category():
         new_category=new_category_entry.get()
         CreateNewCat(new_category)
         # reload categories after adding
         updated_categories = load_categories()
         category_cb['values'] = updated_categories
         if updated_categories:
             category_cb.current(len(updated_categories) - 1)  # Select the newly added category

    def submit_plot():
        CreatePlot()
        
        
        
    #adding the submit button and new category button
    tk.Button(root, text="Add Expense",width=20, command=submit_expense).grid(row=5, column=1,padx=10, pady=5)
    tk.Button(root, text="Add New Category",width=20, command=submit_category).grid(row=6, column=1,padx=10, pady=5)
    tk.Button(root, text="Create Pie Chart",width=20,command=submit_plot).grid(row=7,column=1,padx=10,pady=5)


    #this is to show the first value as the default in categories
    if categories:
        category_cb.current(0)
    root.mainloop()

#This function will load categories from categories csv
def load_categories():
    df = pd.read_csv('data/categories.csv')
    categories=[]
    for cat in df['Category'].dropna().values:
        categories.append(cat)
    return categories        


#This is the function that actually create the database and adds to the database    
def CreateExp(expense, amount, category, date_entry):
    # Create a DataFrame with the expense data
    try:
        output_path='data/expenses.csv'
        file_exists = os.path.exists(output_path)
        
        newExpense = {
            'Expense': [expense],
            'Amount': [float(amount)],
            'Category': [category],
            #'Date': [date]
            'Date': [date_entry]
        }
        #Commenting this out and not writing header everytime
        #df = pd.DataFrame(newExpense,columns=headers_list,index=[1])
        df = pd.DataFrame(newExpense,index=[1])

        # Check if file exists or is non-empty to add appropriate headers
        write_header = not file_exists or os.path.getsize(output_path) == 0

        #This is to add the new expense to the csv
        df.to_csv('data/expenses.csv', mode='a', header=write_header, index=False)
        messagebox.showinfo("Success", "Expense added successfully")
        
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
def CreateNewCat(cat):
    temp=cat.strip()
    output_path='data/categories.csv'

    if os.path.exists(output_path) and os.path.getsize(output_path)>0:
        # Check if the category already exists
        df = pd.read_csv('data/categories.csv')
    else:
        #this creates an empty data frame with the header category
         df = pd.DataFrame(columns=['Category'])

    #now we can drop any existing NAN from the categories
    df.dropna(subset=['Category'],inplace=True)
    
    #for getting the categories as a list instead of a numpy array we use to list
    if temp.lower() in [c.lower() for c in df['Category'].tolist()]:
            messagebox.showerror("Error", "Category already exists")
            return
    if temp=="":
            messagebox.showerror("Error", "Please enter new category")
            return
    if temp==nan:
            messagebox.showerror("Error", "Please enter new category")
            return
    # Add the new category to the DataFrame
    

    
    # newCat={'Category':[temp]}
    # df = pd.DataFrame(newCat)
    # # Append the new category to the CSV file
    # df.to_csv('data/categories.csv', mode='a',header=not os.path.exists('data/categories.csv'),index=False)
    # messagebox.showinfo("Success", "Category added successfully")   
        # If it doesn't exist, append it to the DataFrame
    df = pd.concat([df, pd.DataFrame({'Category': [temp]})], ignore_index=True)
    
    # Save back to CSV
    df.to_csv('data/categories.csv', index=False)
    messagebox.showinfo("Success", "Category added successfully")
    
        
        
    
#this is the function to create expense plots from given data/ pre existing data
def CreatePlot():
    try:
        #this will create a pie chart based on categories
        #will expand late for different types of plots and also date plots or any other metric for plotting
        input_path='data/expenses.csv'
        df=pd.read_csv(input_path)
        column_group=df.groupby("Category")['Amount'].sum()
        fig , ax =plt.subplots(figsize=(8,8))
        explode = [0.05 if i == column_group.idxmax() else 0 for i in column_group.index]
        result=ax.pie(column_group,labels=column_group.index,shadow={'ox': -0.02, 'edgecolor': 'none', 'shade': 1},autopct='%1.1f%%',explode=explode)
        wedges=result[0]
        ax.set_title('Expenses by Category')
        ax.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
        #adding a legend for the plot
        ax.legend(wedges, column_group.index,
          title="Categories",
          loc="lower center",
          bbox_to_anchor=(1,0)
        )
        plt.show()
        
    except FileNotFoundError:
        messagebox.showerror("Error", "Database file not found")
        return
    
#necessary for running ensuring that the program runs properly
if __name__ == "__main__":
    main()
    