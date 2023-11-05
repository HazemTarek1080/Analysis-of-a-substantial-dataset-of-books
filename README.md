# ADM-HW2
This repository contains the source code, notebooks, and additional materials related to Assignment 2 of the "Algorithms for Data Mining" course (23/24) from the Data Science Master's program at Sapienza University of Rome. Below, you will find an overview of the contents of this repository.



## Description
In this assignment, we are analyzing a substantial dataset of books with the aim of extracting valuable insights by addressing specific research questions. This process is designed to provide useful information about the dataset.

The analysis was done to answer the following questions:

  - 8 Research questions: Analysis using Pandas library.
  - Bonus question: Analysis using Dask library.
  - Command Line Question (CLQ): Analysis using command line only.
  - AWS question: A comparison between the local machine and the AWS EC2 instance doing the same analysis.
  - Algorithmic Question: A Sorting problem based on certain instructions. 

For a detailed understanding of the assignment requirements and problems, refer to this [link](https://github.com/Sapienza-University-Rome/ADM/blob/master/2023/Homework_2/README.md).

![overflowing-bookcases](https://github.com/Sapienza-University-Rome/ADM/blob/master/2023/Homework_2/img/books_pict.jpg)

## Dataset
The dataset utilized in this context comprises metadata about books and their respective authors, available in JSON files accessible via this [link](https://www.kaggle.com/datasets/opalskies/large-books-metadata-dataset-50-mill-entries). To expedite the analysis, we worked with a randomly-sampled, lighter version of the data, which can be found here [lighter_authors.json](https://adm2023.s3.amazonaws.com/lighter_authors.json) and [lighter_books.json](https://adm2023.s3.amazonaws.com/lighter_books.json), aiming to reduce the time required for analysis.

## Repo content
- ADM-HW2.ipynb: A comprehensive Jupyter notebook that presents a detailed analysis of the dataset. It includes a systematic breakdown of the analysis process, the resulting insights, accompanying explanations, and graphical representations to give a better understanding of the findings.
  
- aws.py: The script employed for addressing the AWS-related question. You can execute it both on your local machine and your EC2 instance to assess their respective performances. A step-by-step guide on how to perform this comparison can be found in the "AWS question" section within the Jupyter Notebook.

- functions.py: A Python script containing all the functions that were required for our analysis. These functions have been organized in this file to enhance code readability and maintain a tidy structure.

- commandline_original.sh: A PowerShell script that answers the Command Line Question.

- commandline_LLM.sh: A PowerShell script written by a Large Language Model(LLM) to answer the Command Line Question.

## Usage
- Download the JSON files using this [link](https://www.kaggle.com/datasets/opalskies/large-books-metadata-dataset-50-mill-entries).
- clone the repo using the command **git clone https://github.com/Marioiacobelli/ADM-HW2** in a bash script terminal.
- Make sure that the JSON files and the repo content are in the same directory to avoid file accessing errors.
- Open the Jupyter Notebook using your desired IDE and start following the instructions there in order to replicate the results.
- for the AWS Question, make sure to be enrolled in an AWS academy course in order to be able to access the AWS services and create the EC2 instance required. 

## Collaborators
- Hazem Aboulfotouh (aboulfotouh.2105193@studenti.uniroma1.it)
- Francesco Lazzari (lazzari.1917922@studenti.uniroma1.it)
- Mario Iacobelli (Iacobelli.1841427@studenti.uniroma1.it)
- Ana Carina Branescu (branescu.2125078@studenti.uniroma1.it)


