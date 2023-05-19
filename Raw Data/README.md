## Contents of this directory:
1. Barchart-downloads:<br>
This contains the raw datafiles we downloaded from barchart.com in a csv format.
2. Other:<br>
This contains the raw datafiles we downloaded from other sources (Yahoo maybe i dont remember)
3. build_sqlite_db.ipynb:<br>
This is the jupyter notebook which build a sqlite database using some of theraw datafiles from the Barchart-downloads folder.

## Database Description
- SQLITE DATABASE : 'etf_data.db'
- TABLES: SPY,TLT,HYG,LQD,VNQ
- COLUMNS: date, open, high, low, last_traded_price, daily_change, daily_perct_change, volume
- Date Range:<br>
| ETF | Start Date | End Date |
|-----|------------|------------|
| spy | 2000-01-03 | 2023-04-24 |
| tlt | 2002-07-29 | 2023-04-24 |
| hyg | 2007-04-12 | 2023-04-24 |
| lqd | 2002-07-29 | 2023-04-24 |
| vnq | 2004-09-30 | 2023-04-24 |
