# TurboTax Automation
This repo is designed to store any automation tools I've designed for TurboTax

## t5008.py
This script is designed to quickly input all stocks that were traded from the previous year into the T5008 section for Canadian Income Taxes. 

### Requirements 
Python 3  
Properly Formatted Input Data  
Selenium  
```
pip install selenium
```

### Input Data
The input for the script is designed to be taken from a WealthSimple T5008 Tax form and pasted into a txt file.   
Sample Format:  
```
03/11 SHS 1.0000 Gamestop Corporation (Class A) $96.83 CAD $298.00 CAD
```
03/11 = Month/Day of Disposition  
SHS = Type Code of Securities  
1.0000 = Quantity of securities  
Gamestop Corporation (Class A) = Identification of Securities  
$96.83 CAD = Cost or Book Value  
$298.00 CAD = Proceeds or Settlement  
    
Each entry must be contained on a new line
