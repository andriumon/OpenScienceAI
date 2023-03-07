# PDF Processing Software

## Abstract

Software that processes papers in PDF format by calling Grobid's web service and makes a wordcloud for each of them as well as giving a graph indicating the number of figures per article and a list of links found in all of them.

## Important

Papers used for input must have an abstract section or the software will fail

## Instructions

1. Copy this repo in whichever directory you like
2. Create a folder called "pdfs" and put inside the papers you want to process
3. Install [Grobid's Python Client](https://github.com/kermitt2/grobid_client_python)
4. Go to the src folder and run the script
>> `git clone `
>> `cd src`
>> `py pdfProcessing.py`

You can check the results in the folders wordclouds, figures and links, which will be created after you run the script.
