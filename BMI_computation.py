from datetime import datetime
import pandas as pd
import numpy as np
import pickle


class BMI_computation:
    def __init__(self, data, save_loc='results_temp', prints=True):
        
        # Hyperparameters ----------------------------------------------------------------------------------------++
        self.start_time     = datetime.now()
        self.data           = data 
        self.save_loc       = save_loc
        self.BMI_categories = {
        18.4:   {'BMI Category':'Underweight',              'Health risk':'Malnutrition risk'},
        24.9:   {'BMI Category':'Normal weight',            'Health risk':'Low risk'},
        29.9:   {'BMI Category':'Overweight',               'Health risk':'Enhanced risk'},
        34.9:   {'BMI Category':'Moderately obese',         'Health risk':'Medium risk'},
        39.9:   {'BMI Category':'Severly obese',            'Health risk':'High risk'},
        999999: {'BMI Category':'Very severely obese',      'Health risk':'Very high risk'}}
        if prints:
            print('---------------------------------------------------------------------------------------------------++')
            print('Execution BMI computation')
        # Hyperparameters ----------------------------------------------------------------------------------------++

        # Execute ------------------------------------------------------------------------------------------------++
        try:
            mp  = list(map(self.compute_BMI, enumerate(self.data)))
            mp  = [m for m in mp if m is not None]
            df  = pd.DataFrame(mp)
            fig = df.plot(kind='hist', title='Health distribution').get_figure()
            if prints:
                print('Executed successfully.')
        except Exception as e:
            print('failed to execute module.')
            print(f'Exception: {e}')
        # Execute ------------------------------------------------------------------------------------------------++

        # Store --------------------------------------------------------------------------------------------------++
        try:
            fig.savefig(f'{save_loc}/health_distribution.png')
            df.to_csv(f'{save_loc}/processed_dataframe.csv')
            with open(f'{save_loc}/processed_data.pkl', 'wb') as f:
                pickle.dump(mp, f)
            self.end_time = datetime.now()
            if prints:
                print('Saved successfully.')
                print('Runtime: {}'.format(self.end_time - self.start_time))
                print('---------------------------------------------------------------------------------------------------++')
        except Exception as e:
            print('failed to save module.')
            print(f'Exception: {e}')


        # Store --------------------------------------------------------------------------------------------------++

    def switcher(self, bmi):
        for key,val in self.BMI_categories.items():
            if bmi <= key:
                return val['BMI Category'], val['Health risk']
            

    def compute_BMI(self,i,d):
        bmi                         = d['WeightKg']/((d['HeightCm']/100)**2)
        bmi_category, health_risk   = self.switcher(bmi)
        return i, bmi, bmi_category, health_risk

    def compute_BMI(self, id):
        try:
            i, d                        = id
            result                      = d.copy()
            bmi                         = d['WeightKg']/((d['HeightCm']/100)**2)
            bmi_category, health_risk   = self.switcher(bmi)
            result['BMI']               = bmi
            result['BMI Categories']    = bmi_category
            result['Health risk']       = health_risk
            return result
        except:
            print(f'failed to parse entry at index: {i}')
            return None