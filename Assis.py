import cohere
import cx_Oracle

# Configuration for Cohere API
COHERE_API_KEY = '---------------'  # Replace with your Cohere API key

# Oracle Database connection details
DB_CONFIG = {
    "user": "-----",                    # Your Oracle username
    "password": "--------",            # Your Oracle password
    "dsn": cx_Oracle.makedsn("0.0.0.0", 123456789, service_name="Oracle Database Name")  # Using Oracle SID/service
}

# Connect to Cohere API
co = cohere.Client(COHERE_API_KEY)

# Connect to Oracle Database
def connect_to_oracle():
    try:
        conn = cx_Oracle.connect(**DB_CONFIG)
        print("Connected to Oracle Database!")
        return conn
    except cx_Oracle.Error as e:
        print(f"Error connecting to Oracle: {e}")
        return None

def process_prompt(prompt):
    """
    Send the user's prompt to Cohere to generate a database query or response.
    """
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
    )
    return response.generations[0].text.strip()

def query_database(conn, query):
    """
    Execute the generated query on the Oracle database and fetch results.
    """
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except cx_Oracle.Error as e:
        print(f"Database query error: {e}")
        return None

def main():
    conn = connect_to_oracle()
    if not conn:
        return

    print("Welcome! Type your query or task for the AI assistant.")
    
    while True:
        user_prompt = input("\nEnter your query (or type 'exit' to quit): ")
        if user_prompt.lower() == 'exit':
            break
        
        # Step 1: Generate the query using Cohere
        ai_prompt = (
            f"Create an SQL query to {user_prompt}. Assume the database has tables "
            "like employees(employee_id, first_name, last_name, salary) and departments(department_id, name)."
        )
        try:
            generated_query = process_prompt(ai_prompt)
            print(f"\nGenerated SQL Query:\n{generated_query}")
            
            # Step 2: Query the database
            db_result = query_database(conn, generated_query)
            if db_result:
                print("\nDatabase Output:")
                for row in db_result:
                    print(row)
        except Exception as e:
            print(f"Error: {e}")

    # Close the database connection
    conn.close()
    print("Goodbye!")

if __name__ == "__main__":
    main()
