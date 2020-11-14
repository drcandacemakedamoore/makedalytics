## makedalytics
A python library for data analytics on data including text and/or images with an emphasis on scientific reproducibility. Please note the library is currently evolving, and I am testing new functions. At present the tested functional functions of makedalytics are the following: 

# general functions

remind_ds_libraries():
  This function takes no argyments and reminds what libraries you may want to import by printing them.
  
packages_to():
    Tells you what your system and packages are.  

biopsy_df(start_row,end_row,column, df):
    Returns only specified area of dataframe
    
understand_df(df):
  This function takes the dataframe as an argument, and produces information on number of columns, rows, data types, existance of nulls etc.

pristine(df,axis_to_zap, modify_index):
    Takes arguments of dataframe(df), 'columns' or 'rows' (axis to zap) and modify_index which can be set to true or false.
    Returns a cleaned dataframe without columns or rows that have nulls.
    
# text and NLP related functions

show_duplicates(df):
    If there are duplicates it will show and tell. 
    
tag_text(text, column):
    Shows you where (what row) certain text is in a columns. Works like nuclear medicine tagging. 

wordish_count(str):
    counts split up elements of a string. In the case ofan English sentance that is a count for each word with some counting of certain punctuation.

# image related functions   

create_matrix(width, height, default_element):
    Helper function to create matrices `width' x `height' y
    fills with default element which can be set to a number or a boolean (True or False) 
