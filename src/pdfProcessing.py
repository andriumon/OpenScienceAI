from grobid_client.grobid_client import GrobidClient
import xml.etree.ElementTree as ET
import os
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as pyplot



def checkPDF(currentPath):
    for pdf in os.listdir(currentPath+'/pdfs'):
        ext = pdf.split('.')
        if ext[1] != 'pdf':
            print('Error: there is a file that is not a pdf')
            return False
    return True


def keywordClouds(currentPath):

    '''Stopwords config for wordcloud'''

    stopwords = STOPWORDS
    stopwords.add('et')
    stopwords.add('al')


    '''If wordclouds folder doesn't exist, it gets created'''

    if not(os.path.exists(currentPath+'/wordclouds')):
        os.mkdir(currentPath+'/wordclouds')


    for xml in os.listdir(currentPath+'/papers'):
        tree = ET.parse(currentPath+'/papers/'+xml)
        root = tree.getroot()
        element = root.find('.//{http://www.tei-c.org/ns/1.0}abstract/{http://www.tei-c.org/ns/1.0}div/{http://www.tei-c.org/ns/1.0}p')
        text = element.text

        wc = WordCloud(background_color = 'white', stopwords = stopwords, height = 600, width = 600)
        wc.generate(text)
        if not(os.path.exists(currentPath+'/wordclouds/'+xml+'_keyword_cloud.png')):
            wc.to_file(currentPath+'/wordclouds/'+xml+'_keyword_cloud.png')


def figuresPerArticle(currentPath):
    y = []
    x = []
    i = 1


    '''If figures folder doesn't exist, it gets created'''

    if not(os.path.exists(currentPath+'/figures')):
        os.mkdir(currentPath+'/figures')

    for xml in os.listdir(currentPath+'/papers'):
        n = 0
        tree = ET.parse(currentPath+'/papers/'+xml)
        root = tree.getroot()
        x.append('Paper'+str(i)+'')
        i += 1
        for element in root.findall('.//{http://www.tei-c.org/ns/1.0}figure'):
            n += 1
        y.append(n)

    pyplot.bar(x, y, label = 'Number of Figures')
    pyplot.title('FIGURES PER ARTICLE')
    pyplot.savefig(currentPath+'/figures/figsPerArticle.png')


def listOfLinks(currentPath):

    '''If links folder doesn't exist, it gets created'''

    if not(os.path.exists(currentPath+'/links')):
        os.mkdir(currentPath+'/links')

    linkList = []

    for xml in os.listdir(currentPath+'/papers'):
        tree = ET.parse(currentPath+'/papers/'+xml)
        root = tree.getroot()
        for element in root.findall('.//{http://www.tei-c.org/ns/1.0}p'):
            text = element.text
            splitText = text.split()
            for word in splitText:
                if 'https://' in word:
                    if word[-1] == '.':
                        new_word = word.replace(word[-1], '')
                        linkList.append(new_word)
                    else:
                        linkList.append(word)
                        
    content = '\n'.join(linkList)
    file = open(currentPath+'/links/listOfLinks.txt', 'w')
    file.writelines(content)


#SCRIPT
currentPath = os.getcwd()

'''Check if all the files are in pdf format'''

if(checkPDF(currentPath)):

    '''If papers folder doesn't exist, it gets created'''

    if not(os.path.exists(currentPath+'/papers')):
        os.mkdir(currentPath+'/papers')


    '''Service request, input id the directory in which the pdfs are stored, output is the papers folder which
    will be used later as an input for the processing''' 

    client = GrobidClient(config_path='./grobid_client_python/config.json')
    client.process('processFulltextDocument', currentPath+'/pdfs', currentPath+'/papers', n=20)


    keywordClouds(currentPath)
    figuresPerArticle(currentPath)
    listOfLinks(currentPath)
