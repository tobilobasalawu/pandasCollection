import pandas as pd #importing pandas module
import numpy as np #importin numpy module


# Define the structure with the estimated hours and tasks provided earlier
tasks_data = {
    "Mile Stone": [
        "Setup", "Setup", "Setup", "Setup",
        "Model 1", "Model 1", "Model 1", "Model 1",
        "Model 2", "Model 2", "Model 2", "Model 2",
        "Testing", "Testing", "Testing", "User Training", "User Training"
    ],
    "Task": [
        "Upgrade head office infrastructure",
        "Install and configure physical server",
        "Testing hardware",
        "Create Test Plan",
        "Develop module 1: Back-end database",
        "Develop module 2: Maintenance management",
        "Develop module 3: User interface",
        "Develop module 4: Data analysis",
        "Deploy modules",
        "Installation of hardware at two UK airports",
        "Unit Testing",
        "Integration Testing",
        "Fixing and regression testing for major fault",
        "Fixing and regression testing for minor faults",
        "Create a Test Plan",
        "User/Acceptance Testing",
        "Staff Training"
    ],
    "Hours": [40, 40, 56, 7, 100, 95, 50, 105, 28, 60, 48, 64, 48, 20, 28, 13, 15],
    "Staff": [
        "Hou Zijin", "Hou Zijin", "Hou Zijin", "Hou Zijin",
        "Darren Long", "Zuzanna Misaczek", "Peter Evans", "Darren Long",
        "Ellis Soto", "Hou Zijin", "Ellis Soto", "Ellis Soto",
        "Ellis Soto", "Ellis Soto", "Ellis Soto", "Zuzanna Misaczek", "Zuzanna Misaczek"
    ],
}

# Define the number of hours in a week (7 hours/day * 5 days)
hours_per_week = 7 * 5

# Calculate weekly breakdowns
weekly_hours = []
for hours in tasks_data["Hours"]:
    breakdown = []
    remaining_hours = hours
    while remaining_hours > 0:
        if remaining_hours > hours_per_week:
            breakdown.append(hours_per_week)
            remaining_hours -= hours_per_week
        else:
            breakdown.append(remaining_hours)
            remaining_hours = 0
    # Fill weeks with 0 if not using all weeks
    while len(breakdown) < 14:
        breakdown.append(0)
    weekly_hours.append(breakdown)

# Add weekly breakdowns to the DataFrame
weekly_columns = {f"Week {i+1}": [week[i] for week in weekly_hours] for i in range(14)}
tasks_data.update(weekly_columns)

# Create DataFrame for the Gantt chart
gantt_chart_df_complete = pd.DataFrame(tasks_data)

# Display the completed Gantt chart structure
print(gantt_chart_df_complete)
