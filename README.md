## Goal of this project:
1. Build natural language query to an ETF SQLite database we build.
2. Build a streamlit front end for it

### Sample natural language questions:
1. Top performing ETF last year
2. Did SPY outperform TLT last year ?
3. What happened when Russia Invaded ukraine?

## Description of Repository
- The cells in the jupyternotebook 'Exploration' accesses the raw data and creates a sqlite db.
-----
- SQLITE DATABASE : 'etf_data.db'
- TABLES: SPY,TLT,HYG,LQD,VNQ
- COLUMNS: date, open, high, low, last_traded_price, daily_change, daily_perct_change, volume
------
- Raw Data contains the raw data from barchart.com. Data is downloded in csv format
- The other folders are empty directories that are created to manage the entire project.


This README.md will be updated whenever a new update is made.
