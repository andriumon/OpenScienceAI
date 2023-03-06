from grobid_client.grobid_client import GrobidClient
import xml.etree.ElementTree as ET
import os
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as pyplot


#DONE
def keywordClouds(currentPath):

    '''Se configuran las stopwords para la wordcloud'''

    stopwords = STOPWORDS
    stopwords.add('et')
    stopwords.add('al')


    '''Se crea la carpeta en la que se guardaran los wordclouds si no existe ya'''

    if not(os.path.exists(currentPath+'/wordclouds')):
        os.mkdir(currentPath+'/wordclouds')


    '''Algoritmo para crear una wordcloud por cada xml que ha devuelto Grobid'''

    for xml in os.listdir(currentPath+'/papers'):
        tree = ET.parse(currentPath+'/papers/'+xml)
        root = tree.getroot()
        element = root.find('.//{http://www.tei-c.org/ns/1.0}abstract/{http://www.tei-c.org/ns/1.0}div/{http://www.tei-c.org/ns/1.0}p')
        text = element.text

        wc = WordCloud(background_color = 'white', stopwords = stopwords, height = 600, width = 600)
        wc.generate(text)
        if not(os.path.exists(currentPath+'/wordclouds/'+xml+'_keyword_cloud.png')):
            wc.to_file(currentPath+'/wordclouds/'+xml+'_keyword_cloud.png')


#DONE
def figuresPerArticle(currentPath):
    y = []
    x = []
    i = 1


    '''Se crea la carpeta en la que se guardaran las graficas si no existe ya'''

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

    '''Se crea la carpeta en la que se guardaran los links si no existe ya'''

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
                    if word[-1] is '.':
                        new_word = word.replace(word[-1], '')
                        linkList.append(new_word)
                    else:
                        linkList.append(word)
                        
    content = '\n'.join(linkList)
    file = open(currentPath+'/links/listOfLinks.txt', 'w')
    file.writelines(content)


#SCRIPT
currentPath = os.getcwd()

'''Se comprueba que todos los archivos del input sean pdfs'''

for pdf in os.listdir(currentPath+'/pdfs'):
    ext = pdf.split('.')
    if ext[1] is not 'pdf':
        print('Error: there is a file that is not a pdf')
        exit()

'''Se comprueba si hay creada ya una carpeta papers en la que guardar los xmls'''

if not(os.path.exists(currentPath+'/papers')):
    os.mkdir(currentPath+'/papers')


'''Se llama al cliente, pasandole como input el directorio en el que estan los papers(pdf)
   y output el directorio que utilizará el script para coger los xmls que devuelve Grobid''' 

client = GrobidClient(config_path='./grobid_client_python/config.json')
client.process('processFulltextDocument', currentPath+'/pdfs', currentPath+'/papers', n=20)


keywordClouds(currentPath)
figuresPerArticle(currentPath)
listOfLinks(currentPath)
