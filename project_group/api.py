def api_function():

    """
    Function has no given parameter, 
    returns the currency exchange rate by accessing the nested dict (from URL)
    """
    import requests
    from pathlib import Path
    # Access the file "summary_report.txt"
    fp_summary = Path.cwd()/"project_group"/"summary_report.txt" 
    # Assigning url variable a value 
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey='OWNAPI'
    # Send HTTP requests (make a request to the web page as stated above)
    r = requests.get(url)
    data  = r.json()
    # Acceses the nested dictionary to find the exchange rate
    currency_exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate']) 
    # Open file with .open() to return a file object by providing mode and encoding to the parameter, to be writen and decode/encode using UTF-8
    with fp_summary.open(mode= "w", newline = "") as file:
        # Message to be written in the file
        file.write(f"[REAL TIME CURRENCY EXCHANGE RATE] USD1 = SGD{currency_exchange_rate}")
    # Returns the currency_exchange_rate
    return currency_exchange_rate
