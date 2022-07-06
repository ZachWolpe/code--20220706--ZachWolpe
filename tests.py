from datetime import datetime
import pandas as pd
import numpy as np
import pickle


class tests:
    def __init__(self, data, expected_cols=['Gender', 'HeightCm', 'WeightKg']):
        self.data               = data
        self.expected_cols      = expected_cols
        self.correct_columns    = [True for _ in range(len(data))]
        self.correct_dtypes     = [True for _ in range(len(data))]
        self.idx                = None

    def test_entries(self):
        idx = []
        for d in self.data:
            x = np.mean([c in d for c in self.expected_cols]) == 1
            idx.append(x)
        self.correct_columns = idx
        

    def test_datatypes(self, expected_types=[str, int, int]):
        idx = []
        for i, d in enumerate(self.data):
            try:
                x = np.mean([isinstance(d[c], e) for c,e in zip(self.expected_cols, expected_types)]) == 1
                idx.append(x)
            except Exception as e:
                print(f'failed to parse entry at index: {i}')
                print('Exception:', e)
                idx.append(False)
        self.correct_dtypes = idx

    def correct_idx(self):
        self.idx = [i and j for i,j in zip(self.correct_columns, self.correct_dtypes)]

    def filter_data(self):
        self.filtered_data = [d for d,i in zip(self.data, self.idx) if i]

        