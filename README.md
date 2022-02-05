# Algorithms A.Y. 2021/22 
## Software project : A Stock Market Analyzer 

Release V1 - Compute Min, Max and Mean of price.  




## Project structure 
The project has the following structure:
```bash
.
├── README.md
├── data
│   └── small_dataset.txt
├── group0
│   ├── project.py
│   └── utils.py
├── main.py
├── private
│   ├── proutils.py
│   └── solutions.py
├── results
└── results_gold
    ├── proj_v1_AAPL_target.png
    ├── proj_v1_FB_target.png
    └── proj_v1_TSLA_target.png
```

We are providing you a skeleton of the code. You can modify the code we provide, adding the
missing parts. In the project folder, you will find a file main.py (used to run the project) 
and the input file data/small_dataset.txt
You should not change the main file, except for the variable group_id (as specified below).
Change the name of folder group0 to match the group id that we will assign you after the
registration on Luiss Learn, and also change the group_id value in main.py.

Implement your code in file groupid/project.py, that contains two functions (you can add more functions, if
needed, but you must at least implement these ones). Function prepare will be called once to load the dataset: 
use prepare to read the input file (e.g., data/small_dataset.txt) and store the relevant information in suitable global data
structures of your choice. Function stock_stats should implement your query algorithm, as
described in the project pdf. It receives as input the stock name (e.g., AAPL) and it outputs
the observed min, mean, max of the price. The order of the output is important!  

You can use additional files, if needed, but all of them have to be in the group folder. There is a file
utils.py where, if you want, you can implement auxiliary algorithms and data structures.

You can use Python lists, dictionaries, and string functions, but no specific algorithm from any
Python library. If you need any algorithms (e.g., for searching, sorting, or selection) you have to
implement your own version from scratch. If in doubt, just ask.

When you run the main.py script you receive a textual feedback about your solution (e.g., wrong or correct, and expected results).
Moreover, in the folder "results/" the script will generate a set of picture with the conducted analysis, using your results.
You can compare such pictures with the expected ones in the folder "results_gold/"

## Libraries
The code is tested with python3.9.1, you may need to execute the following commands to install libraries and packages:

```bash
pip install pandas
pip install seaborn
pip intsall numpy
pip install matplotlib
```

## Execution

```bash
python3 main.py
```

## Contacts
For further information contact Andrea Coletta at **acoletta[AT]luiss.it**; 
Irene Finocchi   **finocchi[AT]luiss.it**.

