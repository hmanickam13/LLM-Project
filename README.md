## Goal of this project:
1. Build natural language query to an ETF SQLite database we build.
2. Build a streamlit front end for it

### Sample natural language questions:
1. Top performing ETF last year
2. Did SPY outperform TLT last year ?
3. What happened when Russia Invaded ukraine?

## How to get this working?
1. Clone the repo
2. Run the setup.sh file (Create .env file in ur directory. Read setup.sh)
3. Run "python config.py"
4. test streamlit web app should launch

This README.md will be updated whenever a new update is made.

## Database Description
- SQLITE DATABASE : 'etf_data.db'
- TABLES: SPY,TLT,HYG,LQD,VNQ
- COLUMNS: date, open, high, low, last_traded_price, daily_change, daily_perct_change, volume

### Notes
- Raw Data contains the raw data from barchart.com. Data is downloded in csv format
- The jupyter notebook 'Exploration' was used to preprocess the raw data and create a simple sqlite database.
