# makedalytics
Python library for data analytics

This is a library with functions for data anaylytics. It has the following functions: 

def remind_ds_libraries():
  This function takes no argyments and reminds what libraries you may want to import by printing them.
    
def understand_df(df):
  This function takes the dataframe as an argument, and produces information on number of columns, rows, data types, existance of nulls etc.
    
def show_duplicates(df):
    If there are duplicates it will show and tell. 

def create_matrix(width, height, default_element):
    Helper function to create matrices `width' x `height' y
    fills with default element which can be set to a number or a boolean (True or False) 
    
def tag_text(text, column):
    Shows you where (what row) certain text is in a columns. Works like nuclear medicine tagging. 

def biopsy_df(start_row,end_row,column, df):
    Returns only specified area of dataframe


def packages_to():
    Tells you what your system and packages are.


def pristine(df,axis_to_zap, modify_index):
    Takes arguments of dataframe(df), 'columns' or 'rows' (axis to zap) and modify_index which can be set to true or false.
    Returns a cleaned dataframe without columns or rows that have nulls.
