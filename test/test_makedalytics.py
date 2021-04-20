# test makedalytics

import pandas as pd
import numpy as np
import pytest
import os


def test_show_duplicates():
    test_dfE = (os.path.join(image_directory,'test_sample_df.csv'))
    test_df = pd.read_csv(test_dfE)
    checked_example = makedalytics.show_duplicates(test_df)
    assert len(checked_example) > 1 

