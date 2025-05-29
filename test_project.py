import pytest
import project
from unittest.mock import patch,mock_open
import os
import pandas as pd
#will use this module to test out the various functions in the project_py module

'''
When using multiple @patch decorators, the mocks are passed into your test function in the reverse order of how the decorators are stacked
'''
#need to patch the messagebox showinfo and showerror to create a headless test that does not trigger GUI
@patch("project.messagebox.showinfo")
@patch("project.messagebox.showerror")
#test input of valid entry, incorrect value entry for error message
def test_valid_exp(mock_error,mock_info,tmp_path):
    data_dir=tmp_path/"data"
    data_dir.mkdir()
    test_file=data_dir/"expenses.csv"

    #writing to file 
    test_file.write_text("")


    with patch("project.os.path.getsize", return_value= 0),\
         patch("project.os.path.exists", return_value= True),\
         patch("project.pd.DataFrame.to_csv") as mock_to_csv : 

        #calling function
        project.CreateExp("Test_exp",100.0,"Test_Cat","12-05-2025")   

        #expecting appropriate info message
        mock_info.assert_called_once_with("Success", "Expense added successfully") 
        mock_error.assert_not_called()

#need to patch the messagebox showinfo and showerror to create a headless test that does not trigger GUI
@patch("project.messagebox.showinfo")
@patch("project.messagebox.showerror")
def test_invalid_exp(mock_error,mock_info,tmp_path):
    data_dir=tmp_path/"data"
    data_dir.mkdir()
    test_file=data_dir/"expenses.csv"

    #writing to file 
    test_file.write_text("")


    with patch("project.os.path.getsize", return_value= 0),\
         patch("project.os.path.exists", return_value= True),\
         patch("project.pd.DataFrame.to_csv") as mock_to_csv : 

        #calling function
        project.CreateExp("Test_exp","dog","Test_Cat","12-05-2025")   

        #expecting appropriate info message
        mock_error.assert_called_once_with("Error", "Please enter a valid amount")
        mock_info.assert_not_called() 
       

#need to patch the messagebox showinfo and showerror to create a headless test that does not trigger GUI
@patch("project.messagebox.showinfo")
@patch("project.messagebox.showerror")
#test newCategory function by inputting existing category, new category and empty input
def test_validenewcat(mock_error,mock_info,tmp_path):
    data_dir=tmp_path/"data"
    data_dir.mkdir()
    test_file=data_dir/"categories.csv"

    #writing to file 
    test_file.write_text("Categories\nTravel\n") 

        # Patch os.path.exists and os.path.getsize
    with patch("project.os.path.exists", return_value=True), \
         patch("project.os.path.getsize", return_value=1), \
         patch("project.pd.read_csv", return_value=pd.DataFrame({"Category": ["Travel"]})), \
         patch("project.pd.DataFrame.to_csv") as mock_to_csv:
        
        # Call function
        project.CreateNewCat("Food")
        
        # Expect success message
        mock_info.assert_called_once_with("Success", "Category added successfully")
        mock_error.assert_not_called()   

#need to patch the messagebox showinfo and showerror to create a headless test that does not trigger GUI
@patch("project.messagebox.showinfo")
@patch("project.messagebox.showerror")
def test_invalidnewcat(mock_error,mock_info,tmp_path):
    data_dir=tmp_path/"data"
    data_dir.mkdir()
    test_file=data_dir/"categories.csv"

    #writing to file 
    test_file.write_text("Categories\nTravel\n") 

    # Patch os.path.exists and os.path.getsize
    with patch("project.os.path.exists", return_value=True), \
         patch("project.os.path.getsize", return_value=1), \
         patch("project.pd.read_csv", return_value=pd.DataFrame({"Category": ["Travel"]})), \
         patch("project.pd.DataFrame.to_csv") as mock_to_csv:
        
        # Call function
        project.CreateNewCat("Travel")

        mock_info.assert_not_called()
        mock_error.assert_called_once_with("Error", "Category already exists") 