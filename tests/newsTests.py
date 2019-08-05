import unittest

import main

"""
1. Rename your authors_and_feeds.py to main.py
2. Create a parse_link function in your file with one argument
3. Retrieve the link.
4. Run it through BeautifulSoup, end with the visible text of the page
5. Apply SpaCy/textblob's NER functionality and retrieve the people and places mentioned in the url in the desired format.
"""

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
