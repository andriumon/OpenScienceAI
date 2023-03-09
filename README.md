# PDF Processing Software

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7708015.svg)](https://doi.org/10.5281/zenodo.7708015)
[![Documentation Status](https://readthedocs.org/projects/openscienceai/badge/?version=latest)](https://openscienceai.readthedocs.io/en/latest/?badge=latest)

## Description

Software that processes papers in PDF format by calling Grobid's web service and makes a wordcloud for each of them as well as giving a graph indicating the number of figures per article and a list of links found in all of them.

## Requirements

- Papers used for input must have an abstract section or the software will fail.
- [Docker](https://www.docker.com/) must be installed
- Download the Grobid docker image with 
```console
docker pull lfoppiano/grobid:0.7.2
```

### Dependencies

This build has been developed on Python 3.10 and should work with higher versions.

Python libraries matplotlib and wordcloud must be previously installed.

Dependencies can be found [here](/dependencies/dependencies.txt) to use them to build the environment with Conda

### Conda

You can install [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) to easily install all the dependencies needed on an environment(recommended)

If you don't want to use Conda then skip step 3 from the Instructions segment

## Instructions

1. Copy this repo
```console
git clone https://github.com/andriumon/OpenScienceAI.git
```
2. Go to the repo and then to the src directory
```console
cd OpenScienceAI/src 
```
3. Install dependencies or copy the dependencies file to the src directory and use Conda to do it with
```console
conda create -n newenv  
conda activate newenv  
python3 -m pip install --upgrade pip  
pip install -r dependencies.txt
```
**Note:** If python3 doesn't work, try py  

4. Create a folder called "pdfs" in the src directory and put inside all the papers you want to process
5. Install [Grobid's Python Client](https://github.com/kermitt2/grobid_client_python) there
6. Run Grobid with Docker
```console
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```
7. Run the script
```console
python3 pdfProcessing.py
```

You can check the results in the folders "wordclouds", "figures" and "links", which will be created in the directory after you run the script.

## Workflow

![This is a total mess](/assets/workflow.png "Software's Workflow")

## Contact

Main author and contact: andres.montero.martin@alumnos.upm.es
