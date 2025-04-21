#importing the required libraries
from multiprocessing import Value
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


#This is the main function for calling the other functions and generating the UI
def main():
    ...

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
    ...
    
#this is the function to create expense plots from given data/ pre existing data
def CreatePlot():
    ...


    