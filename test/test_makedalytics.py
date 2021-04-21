# test makedalytics

import pandas as pd
import numpy as np
import pytest
import os
import makedalytics

the_directory =  os.path.join(os.path.dirname(__file__), 'directory')

# def test_show_duplicates():
#     test_dfE = (os.path.join(the_directory,'test_sample_df.csv'))
#     test_df = pd.read_csv(test_dfE)
#     checked_example = makedalytics.show_duplicates(test_df)
#     assert len(checked_example) > 1 



def test_create_matrix():
    moko = makedalytics.create_matrix(5, 5, 5)
    # In python Sequence * Number = Sequence repeated Number of times
    assert len(moko[0:1]) == 1    

