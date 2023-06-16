import os
import csv

budget_analysis = os.path.join("Resources", "budget_data.csv")


#variables
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

#lists to store data
date = []
profit = []
monthly_changes = []

#open CSV
with open(budget_analysis, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #skip header
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in csv_reader:
        #count total number of months
        count = count + 1 
        
        # Append profit information & calculate total profit
        date.append(row[0])
        profit.append(row[1])
        
        total_profit = total_profit + int(row[1])

        #Calculate average change in profits from month to month. Then calulate average change in profits
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit

        #Store monthly changes in a list
        monthly_changes.append(monthly_change_profits)

        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit

        #Calculate average change in profits
        average_change_profits = (total_change_profits/count)
        
        # max and min change in profits with corresponding dates the changes were obeserved
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

       

    #print in terminal
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")

    #text file
    with open('financial_analysis.txt', 'w') as text:
        text.write("----------------------------------------------------------\n")
        text.write("  Financial Analysis"+ "\n")
        text.write("----------------------------------------------------------\n\n")
        text.write("    Total Months: " + str(count) + "\n")
        text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
        text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
        text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
        text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
        text.write("----------------------------------------------------------\n")