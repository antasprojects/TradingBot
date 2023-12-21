# Configuration File
# Investment amount represents the total capital available for the portfolio.
# Modify this value based on your desired investment amount.
Investment = 50000

# List of stock tickers to include in the portfolio.
# Each ticker is associated with a specific company in the comments.
tickers = [
    "BA",    # Boeing Co.
    "CAT",   # Caterpillar Inc.
    "GS",    # Goldman Sachs Group Inc.
    "HD",    # Home Depot Inc.
    "JPM",   # JPMorgan Chase & Co.
    "KO",    # The Coca-Cola Co.
    "NKE",   # Nike Inc.
    "V",     # Visa Inc.
    "WMT",   # Walmart Inc.
    "AMZN"   # Amazon.com, Inc.
]

# The following values are used to calculate the desired portfolio allocation.
# You can modify these values to increase or decrease the impact of sentiment on portfolio allocation.

limit = 0.5

# The 'multiplier' determines the strength of the sentiment impact on portfolio allocation.
# A higher multiplier will result in more significant adjustments based on sentiment values.
multiplier = 3