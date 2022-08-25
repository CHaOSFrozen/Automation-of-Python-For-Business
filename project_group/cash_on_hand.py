def coh_function(forex):
    """
    When function is executed, the program will compute the difference in cash-on between each day.
    It would return CASH SURPLUS or CASH DEFICIT depending on the values. If deficit is equal to 0, 
    It would return CASH SURPLUS, otherwise it would return CASH DEFICIT. 
    
    
    """
    # Import path method from Pathlib
    from pathlib import Path
    # Import regular expression and csv from python
    import re, csv
    # Assigning a variable to file path of current working directory 
    file_path = Path.cwd()/"project_group"/"csv_reports"/"Cash_On_Hand.csv"
        
    # Assigning a variable to file path of directory that would be appended
    fp_summary = Path.cwd()/"project_group"/"summary_report.txt"
    
    # Creates two variables, increment & deficit
    increment = 0
    deficit = 0
    # Creates empty list  
    cash_on_hand = []

    # Start of Exceptional Handling
    try:

        # Opens files with .open() with read mode to return a file object 
        with file_path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
            # Instantiate a reader object
            reader = csv.reader(file)
            # Return the next item from the iterator 
            next(reader)

            for value in reader:
                cash_on_hand.append(value)
            # Returns the number of items in the reader object
            length = len(cash_on_hand)
            # Iterates through one line and then the next line after first round of iteration. 
            while increment + 1 < length: 
                # Creates two variables, value1 & value2 assinging values of previous and current day
                value1 = float((cash_on_hand[increment][1]))
                value2 = float(cash_on_hand[increment + 1][1])
                # Checks if previous day value is greater than current day
                condition = value1 >  value2
                # Deficit will be calculated if condition is met
                if condition:
                    deficit = value1 -  value2
                    # Opening file in append mode with encoding "UTF-8" to return a file object
                    with fp_summary.open(mode="a", encoding = "UTF-8", newline = "") as file:
                    # Writes a message in the file
                        message = f"\n[CASH DEFICIT] DAY: {cash_on_hand[increment + 1][0]}, AMOUNT: SGD{(deficit * forex):.2f}"
                        # Writes the message, above in the file
                        file.write(message.upper())
                        # Closes the file
                        file.close()
                # Adding one on every iteration, until last iteration
                increment += 1
                # If defiit equals to 0
            if deficit == 0:
                # Opening file in append mode with encoding "UTF-8"
                with fp_summary.open(mode="a", encoding = "UTF-8", newline = "") as file:
                    message = (f"\n[CASH SURPLUS] cash on hand is higher than the pervious day")
                    # Writes the message in the file with upper case
                    file.write(message.upper())
                    # Closes the above opened file
                    file.close()
            # Closes the entire file
            file.close()
        # Handling of Exception
    except:
        with fp_summary.open(mode = "a", encoding = "UTF-8", newline = "") as file:
            # Assigning the variable message to the final statement that is meant to be displayed on the final text file
            message = f"\nInvalid Entry. Please try again"
            # Writing data to the final text file in uppercase
            file.write(message.upper())
            # Use '.close()' to close a file
            file.close()
    # Else, Do nothing, when exception does not occur 
    else: 
        pass
    # Finally, Do nothing, when exception does not occur 
    finally: 
        pass
