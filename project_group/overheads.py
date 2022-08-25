def overheads_function(forex):
    # Import path method from pathlib 
    from pathlib import Path
    # Import csv module 
    import csv

    # Assigning a variable to file path of directory that would be appended
    fp_summary = Path.cwd()/"project_group"/"summary_report.txt"
    
    # Assigning a variable to file path of current working directory 
    file_path = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"
    
    # Creates empty list using [] instead of list() to store values to be appended later
    empty_list = []
    overheads_value = []
    # Start of expectional handling
    try: 
        # Opening file in read mode with encoding "UTF-8" 
        with file_path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
            # Instantiate a reader object
            reader = csv.reader(file)
            # Use 'next()' to skip the header
            next(reader)
            # Iterate over the lines of the csv file (processes each line)
            for line in reader:
                # Append values from the CSV at the end of the list
                empty_list.append(line)
                # Access and appends the second value in a line, value of Overheads
                overheads_value.append(float(line[1]))

        for category, overheads in empty_list:
            # Assigns float value to overheads
            overheads = float(overheads)
            # Assigns highestoverheads to the maximum overheads value from the overheads list
            highestoverheads = max(overheads_value)
            # Condition: If overheads is the maximum overheads, will open file and write a message
            if overheads == highestoverheads:
                # Opening file in append mode with encoding "UTF-8" 
                with fp_summary.open(mode = "a", encoding = "UTF-8", newline = "") as file:
                     # Assigning the variable message to the final statement that is meant to be displayed on the final text file
                    message = f"\n[HIGHEST OVERHEADS] {category}: SGD{highestoverheads * forex:.2f}"
                     # Writing data to the final text file in uppercase
                    file.write(message.upper())
                     # Use '.close()' to close a file
                    file.close()
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
