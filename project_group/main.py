# Imports the data of other files. 
import api, cash_on_hand, overheads, profit_loss

def main():

    """
    When function is executed, it would import the codes from other 
    files and run them to return the individual date on the appended text, summary_report.txt.
    """
    # Assigns forex to api function so when called, it would return the converted value for the other files
    forex = api.api_function()
    overheads.overheads_function(forex)
    cash_on_hand.coh_function(forex)
    profit_loss.profitloss_function(forex)

main()
