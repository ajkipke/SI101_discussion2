import unittest
import os
import csv

def load_results(f):
    '''
    Params: 
        f, name or path or CSV file: string

    Returns:
        nested dict structure from csv
        outer keys are (str) races, values are dicts
        inner keys are (str) horse, values are (str) race times
    
    Note: Don't strip or otherwise modify strings. Don't change datatypes from strings. 
    '''
    
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)
    # use this 'full_path' variable as the file that you open

    pass

        
def get_horse_results(d):
    '''
    Params:
        d, dict created by load_csv above

    Returns:
        list of tuples, each with 3 items: race (str), horse (str), and fastest time (int) 
        max is the maximum value of speed for a horse in that race, horse is the corresponding horse with that time

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary.
        TIP: You will need to modify time to a float. 
    '''
    
    pass
        


def get_avg_speed(d):
    '''
    Params: 
        d, dict created by load_csv above

    Returns:
        dict where keys are races and vals are floats rounded to nearest whole number
        vals are the average values for all horses in the race

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary. 
        TIP: You'll have to use the round function for your average.
    '''
    pass
        
            

class dis7_test(unittest.TestCase):
    '''
    you should not change these test cases!
    '''
    def setUp(self):
        self.race_dict = load_results('race_results.csv')
        self.max_tup_list = get_horse_results(self.race_dict)
        self.avg_dict = get_avg_speed(self.race_dict)

    def test_load_csv(self):
        # Outer keys are races
        self.assertIsInstance(self.race_dict['Tenno Sho Fall'], dict)
        # Check one horse's time
        self.assertEqual(self.race_dict['Teio Sho']['Symboli_Rudolf'], '14.8')

    def test_get_horse_results(self):
        # Max horse per race
        expected = [
            ('Tenno Sho Fall', 'Silence_Suzuka', 17.2),
            ('Tenno Sho Spring', 'Silence_Suzuka', 17.5),
            ('Teio Sho', 'Silence_Suzuka', 17.8)
        ]
        self.assertEqual(self.max_tup_list, expected)

    def test_get_avg_speed(self):
        # Average times rounded to nearest integer
        avg_times = get_avg_speed(self.race_dict)
        self.assertEqual(avg_times['Tenno Sho Fall'], round(
            sum([16.5, 17.2, 16.9, 16.1, 16.8, 16.3, 17, 16.7, 16.4, 16.6, 15.5, 15.2])/12))
        self.assertEqual(avg_times['Teio Sho'], round(
            sum([17, 17.8, 17.3, 16.5, 17, 16.7, 17.4, 17, 16.8, 17.1, 15.9, 14.8])/12))


def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
