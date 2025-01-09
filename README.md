AI-Driven SQL Assistant
AI-Driven SQL Assistant is a Python-based project that integrates Cohere AI with Oracle Database to revolutionize database management. It enables users to input plain language prompts, which are converted into accurate SQL queries and executed on an Oracle Database, providing results in real-time. This tool bridges the gap between natural language processing and database interactions, making data management intuitive and efficient.

Key Features
•	AI-Powered SQL Generation: Cohere AI processes natural language prompts and converts them into SQL queries tailored to the database schema.
•	Seamless Oracle Database Integration: Enables secure and efficient connection to Oracle Database for query execution.
•	Interactive Command-Line Interface (CLI): A user-friendly CLI lets users input prompts and see results interactively.
•	Dynamic Query Processing: Supports various SQL query types like SELECT, INSERT, UPDATE, and DELETE.
•	Real-Time Feedback: Immediate generation and execution of queries ensure a smooth user experience.

Technologies Used
•	Python: The core language used for development.
•	Cohere API: Powers the natural language to SQL conversion.
•	cx_Oracle: A Python library for Oracle Database connectivity.
•	Oracle Database: Used for testing and query execution.

How It Works
1.	Natural Language Input: The user enters a prompt (e.g., "List all employees in the Sales department").
2.	AI Processing: The prompt is sent to Cohere's NLP model, which generates the corresponding SQL query.
3.	Database Execution: The generated query is executed on the Oracle Database, and the results are displayed.
________________________________________
Getting Started
Prerequisites
•	Python 3.8 or higher installed.
•	Access to an Oracle Database instance.
•	A valid Cohere API key.
Installation
1.	Clone the repository: 
2.	git clone https://github.com/your-username/AI-Driven-SQL-Assistant.git
3.	Install required dependencies: 
4.	pip install cohere cx_Oracle
Configuration
•	Replace COHERE_API_KEY in the script with your Cohere API key.
•	Update the DB_CONFIG dictionary with your Oracle Database credentials.
Usage
1.	Run the script: 
2.	python main.py
3.	Enter a natural language prompt, such as:
"List the names and salaries of employees earning more than $50,000."
4.	View the generated SQL query and results instantly.
5.	Type exit to end the session.
________________________________________
Example Workflow
Input Prompt:
"Retrieve the names and salaries of employees in the Marketing department."
Generated SQL Query:
SELECT first_name, last_name, salary  
FROM employees  
JOIN departments ON employees.department_id = departments.department_id  
WHERE departments.name = 'Marketing';
Output:
John Doe, 75000  
Jane Smith, 72000  
________________________________________
Security Recommendations
•	Avoid hardcoding sensitive information like API keys or database credentials. Use environment variables for better security.
•	Ensure proper access controls and query validation to prevent SQL injection.
________________________________________
Acknowledgments
•	Cohere AI for their NLP API.
•	Oracle Database for reliable database management solutions.
Let me know if you need further adjustments!

