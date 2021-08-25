# A program that calculates gas mileage based on user input
# 8/25/2021
# CSC121 M1Pro – Miles Per Gallon
# Branden Alder

totalGallons = 0 #initalize accumulators
totalMiles = 0

gallonsUsed = float(input("Enter the gallons used (-1 to end): "))

while gallonsUsed != -1: # while loop using sentinel
    
    totalGallons += gallonsUsed
    
    milesDriven = float(input("Enter the miles driven: "))
    totalMiles += milesDriven
    # Calculate MPG and print using 6 decimal places
    milesPerGallon = milesDriven / gallonsUsed
    print(f"The miles/gallon for this tank was {milesPerGallon:.6f}")
    
    gallonsUsed = float(input("Enter the gallons used (-1 to end): "))
    # Displays overall miles a gallon using 6 decimal places
print(f"The overall average miles/gallon was {totalMiles / totalGallons:.6f}")