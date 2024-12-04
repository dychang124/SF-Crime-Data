import unittest 
import pandas as pd
import numpy as np
from io import StringIO

from crime_correlations import time_frequency, day_of_week_frequency, police_district_frequency

class testFunctions(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame for testing
        data = """Incident Time,Incident Day of Week,Police District
        10:30,Wednesday,Central
        14:45,Friday,Southern
        ,,
        01:15,Monday,Northern
        23:00,Sunday,Mission
        ,Tuesday,
        18:00,Thursday,Richmond
        12:59,Saturday,Park
        invalid_time,Wednesday,Central
        19:00,InvalidDay,Bayview
        """
        self.df = pd.read_csv(StringIO(data))


    def test_time_frequency(self):
        expected_frequencies = {
            "0:00-1:59": 1, "2:00-3:59": 0, "4:00-5:59": 0, "6:00-7:59": 0, "8:00-9:59": 0,
            "10:00-11:59": 1, "12:00-13:59": 1, "14:00-15:59": 1, "16:00-17:59": 0, "18:00-19:59": 1,
            "20:00-21:59": 0, "22:00-23:59": 1
        }
        
        try:
            actual_frequencies = time_frequency(self.df)
            self.assertEqual(actual_frequencies, expected_frequencies)
        except ValueError as e:
            # Expect a ValueError for the "invalid_time"
            self.assertIn("Invalid time format", str(e))

    def test_day_of_week_frequency(self):
        expected_frequencies = {
            "Monday": 1, "Tuesday": 1, "Wednesday": 2, "Thursday": 1, "Friday": 1,
            "Saturday": 1, "Sunday": 1
        }
        actual_frequencies = day_of_week_frequency(self.df)
        self.assertEqual(actual_frequencies, expected_frequencies)
    
    def test_police_district_frequency(self):
        expected_frequencies = {
            'Central': 2, 'Tenderloin': 0, 'Ingleside': 0, 'Park': 1, 'Richmond': 1,
            'Bayview': 1, 'Northern': 1, 'Southern': 1, 'Mission': 1, 'Taraval': 0
        }
        actual_frequencies = police_district_frequency(self.df)
        self.assertEqual(actual_frequencies, expected_frequencies)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
