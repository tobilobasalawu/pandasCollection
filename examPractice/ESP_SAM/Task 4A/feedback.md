Step 1: Understanding the Marking Scheme

A Python-based project like this is usually graded on:
	1.	Code Structure & Organization (10 marks)
	•	Proper function definitions
	•	Logical flow of execution
	•	Modularization (breaking tasks into functions)
	2.	User Input Handling & Validation (15 marks)
	•	Correct handling of user input
	•	Validation checks for incorrect inputs
	•	Appropriate error handling
	3.	Data Handling (15 marks)
	•	Reading CSV files correctly
	•	Extracting relevant data
	•	Handling missing or incorrect data
	4.	Mathematical Accuracy & Currency Conversion (20 marks)
	•	Correct implementation of currency conversion
	•	Accurate calculations
	•	Rounding & formatting of output
	5.	Trends & Visualization (20 marks)
	•	Correct extraction of trend data
	•	Appropriate use of matplotlib
	•	Clear, readable graphs
	6.	Code Readability & Comments (10 marks)
	•	Proper function docstrings
	•	Readable variable names
	•	Code clarity
	7.	Execution Flow & User Experience (10 marks)
	•	Smooth execution of the program
	•	Logical user interaction

Total Marks: 100

⸻

Step 2: Comparing Your Code Against the Marking Scheme

1. Code Structure & Organization (8/10)

✅ Functions are well-defined and modular (e.g., menu(), get_currency(), perform_conversion())
✅ Good function decomposition (each function does one thing)
❌ Minor issue: Some functions like execute_program() could be refactored to be cleaner

2. User Input Handling & Validation (13/15)

✅ Validation is present for menu selection (menu_choice ensures input is between 1-8)
✅ Ensures numerical input for conversion amounts
❌ A small improvement: You could handle invalid file cases better (currently just prints an error message)

3. Data Handling (14/15)

✅ Reads CSV file using pandas
✅ Extracts the latest conversion rates using .iloc[-1]
❌ Missing a return statement in get_conversion_rate() in case the file is not found

4. Mathematical Accuracy & Currency Conversion (18/20)

✅ Conversion is calculated using the latest exchange rate
✅ Rounds to two decimal places
❌ A minor issue: Instead of currency[0:3] and currency[6:9], a more robust approach would be split(' - ')

5. Trends & Visualization (19/20)

✅ Uses pandas to fetch data
✅ Plots trends with matplotlib
✅ Handles user-defined days (1 to 86)
❌ Could improve graph labeling (axis labels could be clearer)

6. Code Readability & Comments (9/10)

✅ Uses docstrings for all functions
✅ Readable variable names
❌ Some docstrings could be clearer (e.g., trends_and_patterns_overtime_menu())

7. Execution Flow & User Experience (9/10)

✅ Logical user flow (select conversion → enter amount → get results)
✅ Error handling prevents crashes
❌ Could improve UX by allowing the user to retry instead of restarting on invalid input

⸻

Final Score: 90/100

Summary of Strengths:
	•	Great modularization with well-structured functions
	•	Strong input validation and error handling
	•	Correct currency conversion logic
	•	Trend analysis and visualization are well-executed

Areas for Improvement:
	1.	Improve robustness of get_conversion_rate() when file errors occur
	2.	Make graph labels more detailed
	3.	Slightly refine execution flow for a smoother user experience
