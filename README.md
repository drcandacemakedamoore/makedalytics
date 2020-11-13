# makedalytics
A python library for data analytics on data including text and/or images with an emphasis on scientific reproducibility. 
makedalytics has the following functions: 

remind_ds_libraries():
  This function takes no argyments and reminds what libraries you may want to import by printing them.
    
understand_df(df):
  This function takes the dataframe as an argument, and produces information on number of columns, rows, data types, existance of nulls etc.
    
show_duplicates(df):
    If there are duplicates it will show and tell. 

create_matrix(width, height, default_element):
    Helper function to create matrices `width' x `height' y
    fills with default element which can be set to a number or a boolean (True or False) 
    
tag_text(text, column):
    Shows you where (what row) certain text is in a columns. Works like nuclear medicine tagging. 

biopsy_df(start_row,end_row,column, df):
    Returns only specified area of dataframe


packages_to():
    Tells you what your system and packages are.


pristine(df,axis_to_zap, modify_index):
    Takes arguments of dataframe(df), 'columns' or 'rows' (axis to zap) and modify_index which can be set to true or false.
    Returns a cleaned dataframe without columns or rows that have nulls.

wordish_count(str):
    counts split up elements of a string. In the case ofan English sentance that is a count for each word with some counting of certain punctuation.
