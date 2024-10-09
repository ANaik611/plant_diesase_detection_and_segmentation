def categorize_area(affected_area, total_area):
    # Calculate the percentage of the affected area
    if total_area == 0:
        return "Total area cannot be zero."

    percentage = (affected_area / total_area) * 100

    # Categorize based on percentage
    if percentage < 0:
        return "Invalid affected area."
    elif percentage <= 4:
        category = "Normal"
    elif percentage <= 20:
        category = "Infected"
    elif percentage <= 40:
        category = "Serious"
    elif percentage <= 60:
        category = "Critical"
    elif percentage <= 80:
        category = "Very Critical"
    else:
        category = "Dead"

    return f"Percentage: {percentage:.2f}%, Category: {category}"

# Example usage:
affected_area = 15  # Input affected area
total_area = 100    # Input total area

result = categorize_area(affected_area, total_area)
print(result)
