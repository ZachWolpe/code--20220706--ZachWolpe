# packages
from datetime import datetime
import pandas as pd
import numpy as np
import pickle
import json 
# modules
from BMI_computation import *
from tests import *

# hyperparameters
save_loc  = 'results_temp'
input_loc = 'data' 


if __name__ == "__main__":
    try:
        with open(f'{input_loc}/data.json', 'r') as f:
            input_data = json.load(f)
        
        # test data
        t = tests(input_data)
        t.test_entries()
        t.test_datatypes()
        t.correct_idx()
        t.filter_data()

        # compute BMI
        BMI_computation(t.filtered_data, save_loc=save_loc)
    except Exception as e:
        print('FAILED. \nNo file \'data.json\' in directory.')