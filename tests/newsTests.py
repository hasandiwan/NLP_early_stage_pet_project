import unittest

import main

class NewsTests(unittest.TestCase):
    def testValidNerKeys(self):
        response = main.parse_link('https://www.theguardian.com/world/2019/jul/31/hamza-bin-laden-son-of-osama-bin-laden-has-died-reports')
        [self.assertIn(p, response) for p in ['people', 'places']]

    def testPeople(self):
        response = main.parse_link("https://www.theguardian.com/world/2019/jul/31/hamza-bin-laden-son-of-osama-bin-laden-has-died-reports")
        [self.assertIn(p, response.get('people')) for p in ['Osama bin Laden', 'Hamza bin Laden']]
    
    def testPlaces(self):
        response = main.parse_link("https://www.theguardian.com/world/2019/aug/01/us-imposes-sanctions-on-irans-foreign-minister-javad-zarif")
        [self.assertIn(p, response) for p in ['Washington', 'Iran', 'US']]
         
if __name__ == '__main__':
  unittest.main()
