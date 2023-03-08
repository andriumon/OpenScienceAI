# PDF Processing Software

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7708015.svg)](https://doi.org/10.5281/zenodo.7708015)

## Description

Software that processes papers in PDF format by calling Grobid's web service and makes a wordcloud for each of them as well as giving a graph indicating the number of figures per article and a list of links found in all of them.

## Requirements

Papers used for input must have an abstract section or the software will fail.

This build has been developed on Python 3.10 and should work with higher versions.

Check the dependencies folder so you can reproduce the environment in which the software was developed.

## Instructions

1. Copy this repo in whichever directory you like
2. Create a folder called "pdfs" and put inside the papers you want to process
3. Install [Grobid's Python Client](https://github.com/kermitt2/grobid_client_python)
4. Go to the src folder and run the script

You can check the results in the folders "wordclouds", "figures" and "links", which will be created in the directory after you run the script.

## Workflow

![The San Juan Mountains are beautiful!](/workflow/workflow.png "Software's Workflow")

## Readthedocs

[![Documentation Status](https://readthedocs.org/projects/openscienceai/badge/?version=latest)](https://openscienceai.readthedocs.io/en/latest/?badge=latest)

## Contact

Main author and contact: andres.montero.martin@alumnos.upm.es
