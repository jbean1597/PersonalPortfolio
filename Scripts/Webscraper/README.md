# Trading Bot Scripts
<br>**Concepts Applied:** Data Gathering, Data Manipulation, API, Financial/Stock Traits </br>
<br>**Languages:** Python, Jupyter Notebook</br>
<br>**Libraries Used:** Alpaca Trade API</br>

## TL;DR
* Trading Bot in progress to automate stock portfolio management, ideally for future implementation in my real portfolio for performance analysis
* First phase is done (Create instance classes for account transactions and allow it to do buys/sells on a Alpaca Paper account


### Final Results 
* This section will be filled out once I complete the automation and progress-tracking portions of the project

## Introduction
This trading bot was born of my own curiosity with the stock market and implementing programming in my life where I think it could significantly help me. I began the process of building it on Alpaca Markets since they have a "paper account" that allows you to simulate trading with fake money. It allows for backtesting and a clear view of how the program will perform in real life before implementation into an actual account since I'd rather not risk that much without any idea of how it performs. The paper account given by Alpaca contains $100,000 in equity and allows you to trade that paper for stocks while tracking your performance just like a real profile; should anything go wrong in the code, all it takes is a simple reset and another fake $100,000 will be put in the account. 

## Code
This code makes simple decisions for buy/sell based on the delta of the stock symbol specified in `self.symbol` and uses 3 verifications for those decisions; if delta is greater that 0 then the stock is bought with the amount of stocks desired(`target`), if delta is less than 0 then it is sold, if delta is 0 then it just prints out a message saying the order is being processed. The orders this program submits are limit orders with a limit price of $1.00.

[Jupyter Notebook of Code](../blob/master/LICENSE)

## Final Performance
* This section will also be filled out when final results are collected.
