import platform
try:
    from pip._internal.operations import freeze
except ImportError:  # pip < 10.0
    from pip.operations import freeze

def remind_ds_libraries():
    print ("Basics: \n import pandas as pd\n import numpy as np\n import matplotlib \n import matplotlib.pyplot as plt\n")
    print("Visualization:\n from IPython.display import Markdown, display \n from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot\n import plotly.graph_objs as go\n import seaborn as sns")
    print("NLP: import re\n import nltk \nfrom nltk.stem import SnowballStemmer \nfrom nltk.stem import WordNetLemmatizer \nfrom nltk import wordpunct_tokenize \n from nltk.corpus import stopwords \n from nltk.tokenize import sent_tokenize, word_tokenize \n from collections import Counter ")
    print("Stats: \n import scipy \n from scipy import stats as st\n")


def understand_df(df):

    print("The table has x entries with y data points- x,y here are:", df.shape)
    print("")
    print("The dataframe has", len(df), "rows")
    print("")
    print("The dataframe has", len(df.columns), "columns, named", df.columns )
    print("")
    print("In terms of nulls, the dataframe has: \n", df.isnull().sum())
    print("")
    print("Number of duplicated rows in the data is: \n",  df[df.duplicated()].count(), ".")
     print("")
    print("The types of data:\n", df.dtypes)
    print("")
    print("Numeric qualities of numeric data: \n", df.describe()) 
    
    
def show_duplicates(df):
    if df.duplicated().any():
        print("This table has duplicated rows, so let me show them", df.duplicated())
    else:
        print("There are no duplicated rows")   

def create_matrix(width, height, default_element):
    '''
    Helper function to create matrices `width' x `height' big
    filled initially with `default_element'
    '''
    # In python Sequence * Number = Sequence repeated Number of times
    result = [0] * width

    for i in range(width):
        result[i] = [default_element] * height

    return result

def tag_text(text, column):
    finds = []
    for number, row in enumerate(column):
        found = text in row
        if found:
            finds.append([number, row])
    return finds      


def biopsy_df(start_row,end_row,column, df):
    range_rows = range(start_row,end_row) 
    finds = df.loc[range_rows]
    return finds[column]


def packages_to():
    platform_sys = platform.system()
    release = platform.release()

    print("System Platform:", platform_sys, release)
    print("Packages:") 
    x = freeze.freeze()

    with open("requirementscontext.txt", 'w') as f:
        for p in x:
            print(p)
            f.write(str(p))
            f.write('\n')


def pristine(df,axis_to_zap, modify_index):
    if modify_index == False:  # if true reset in place, if false don't
        df = df.dropna(axis = axis_to_zap, inplace = False).reset_index()
        df.drop_duplicates(inplace=True)
    else: 
        df = df.dropna(axis = axis_to_zap, inplace = False)
        df.drop_duplicates(inplace=True)
    return df
