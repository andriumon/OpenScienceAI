# Review

The software has been tested with 9 papers from Google Scholar and works properly. More about that below:

## Observations and limitations

- If one or more PDFs do not have an abstract field the software will fail. Due to this, the software has been updated to check if all the inputs are correct
- The links gotten in the txt file are the ones that are under the tag \<p\> in the TEI file generated when calling Grobid. There are more which can be found just by looking at the TEI files but no solution has been found yet
  
## Results

![Example figure 1](/assets/pdfsExample.png)

### Wordcloud

As shown here, you can see that a wordcloud has been created for each pdf file given as input

![Example figure 2](/assets/wcExample.png)


### Graphic

In this image, you can see the bar graphic created by the software. Paper5, which is the nectin_analysis pdf from the image showed above, has only 2 figures that
are marked with the \<figure\> tag in its TEI file

![Example figure 3](/assets/figsPerArticle.png)


### List of links

The resulting list of links only shows 1 link from the nectin_analysis pdf
  
