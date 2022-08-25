def profitloss_function(forex):   

    """ 
    When function is executed, it would compute the difference in the net profit between each day
    and would highlight the the day(s) when net profit is lower than the previous day. It would also 
    highlight the value of the difference.
    """
    
    # Import path method from Pathlib
    from pathlib import Path
    # Import request and csv from python
    import re, csv
    # Assigning a variable to file path of current working directory 
    file_path = Path.cwd()/"project_group"/"csv_reports"/"Profit&Loss.csv"
    # Assigning a variable to file path of directory that will be appended
    fp_summary = Path.cwd()/"project_group"/"summary_report.txt" 

    # Creates two variables, increment & shortage and assigns the value zero
    increment = 0
    shortage = 0
    #  Creates empty list to be used for appending later 
    profitloss = []
    try: 
        # Opening file in read mode with encoding "UTF-8"
        with file_path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
            # Create a reader object and named it as 'reader' variable. (instantiate a reader object)
            reader = csv.reader(file)
            # Use 'next()' to skip the header from the iterator 
            next(reader)

            for value in reader:
                profitloss.append(value)
            # Returns the number of items in an object, profitloss
            length = len(profitloss)
            # Iterates thorugh all the days (lines) until the very last day, day 45 in the list 
            while increment + 1 < length:
                # Creates two variables and assigns values for previous day and current day 
                coverted1 = float((profitloss[increment][4]))
                coverted2 = float(profitloss[increment + 1][4])
                # Condition: Checks if current day is lesser than previous day 
                condition = coverted1 >  coverted2
                # If condition is met, will follow the steps shown below.
                if condition: 
                    # Assigns the difference in values if condition is met, to deficit 
                    shortage = coverted1 - coverted2
                    # Opening file in append mode with encoding "UTF-8"
                    with fp_summary.open(mode="a", encoding = "UTF-8", newline = "") as file:
                        # Message to be appended on to the file, and using the round function, it rounds to the nearest 2 d.p.
                        message = f"\n[PROFIT DEFICIT] DAY: {profitloss[increment + 1][0]}, AMOUNT: SGD{(shortage * forex):.2f}"
                        # Writes the message on the file
                        file.write(message)   
                        # Closes the files    
                        file.close()
                # Adding one on every iteration until requirements are met (while increment + 1 < length)
                increment += 1
            # if deficit equals to 0 (zero), conditon is met, follow the steps shown below
            if shortage == 0:
                # Opening file in append mode with encoding "UTF-8"
                with fp_summary.open(mode="a", encoding = "UTF-8", newline = "") as file:
                    message = f"\n[PROFIT SURPLUS] net profit on each day is higher than the previous day"
                    # Writes the message on the file in upper case 
                    file.write(message.upper())
                    # Closes the fp_summary file 
                    file.close()
        # Closes the entire file
    # Handling of Exception
    except:
        with fp_summary.open(mode = "a", encoding = "UTF-8", newline = "") as file:
            # Assigning the variable message to the final statement that is meant to be displayed on the final text file
            message = f"\nInvalid Entry. Please try again"
            # Writing data to the final text file in uppercase
            file.write(message.upper())
            # Use '.close()' to close the file
            file.close()
    # Else, Do nothing, when exception does not occur 
    else: 
        pass
    # Finally, Do nothing, when exception does not occur 
    finally: 
        pass
