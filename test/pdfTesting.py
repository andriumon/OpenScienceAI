import unittest
import os
from pdfProcessing import checkPDF, keywordClouds, listOfLinks, figuresPerArticle

class tests(unittest.TestCase):

    '''Check if input is right'''

    def testPDF(self):
        currentPath = os.getcwd()
        bool = checkPDF(currentPath)
        self.assertTrue(bool)

    '''Check if wordclouds are created'''

    def testWordcloud(self):
        currentPath = os.getcwd()
        keywordClouds(currentPath)
        i = 0
        for wc in os.listdir(currentPath+'/wordclouds'):
            i += 1
        self.assertEqual(i, 8)

    def testLinks(self):
        currentPath = os.getcwd()
        listOfLinks(currentPath)
        self.assertGreater(os.path.getsize(currentPath+'/links/listOfLinks.txt'), 0)

if __name__ == '__name__':
    unittest.main()

