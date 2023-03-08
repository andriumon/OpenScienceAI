# PDF Processing Software

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7708015.svg)](https://doi.org/10.5281/zenodo.7708015)
[![Documentation Status](https://readthedocs.org/projects/openscienceai/badge/?version=latest)](https://openscienceai.readthedocs.io/en/latest/?badge=latest)

## Description

Software that processes papers in PDF format by calling Grobid's web service and makes a wordcloud for each of them as well as giving a graph indicating the number of figures per article and a list of links found in all of them.

## Requirements

Papers used for input must have an abstract section or the software will fail.

### Dependencies

This build has been developed on Python 3.10 and should work with higher versions.

Python libraries matplotlib and wordcloud must be previously installed.

Check the [dependencies file](/dependencies/dependencies.txt) for a more extense list of dependencies of the environment in which the software was developed.

## Instructions

1. Copy this repo
2. Go to the repo and then to the src directory
2. Create a folder called "pdfs" in said directory and put inside the papers you want to process
3. Install [Grobid's Python Client](https://github.com/kermitt2/grobid_client_python) there
4. Run the script

You can check the results in the folders "wordclouds", "figures" and "links", which will be created in the directory after you run the script.

## Workflow

![This is a total mess!](/assets/workflow.png "Software's Workflow")

## Contact

Main author and contact: andres.montero.martin@alumnos.upm.es
