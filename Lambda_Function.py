import json
import pandas as pd
from io import StringIO

# The lambda_handler is the main function that AWS Lambda runs when triggered.
# The 'event' object contains all the information from the API Gateway,
# including the CSV data sent from the webpage.
def lambda_handler(event, context):
    """
    This function is triggered by an API Gateway. It reads CSV data from the
    request body, processes it using Pandas to calculate the average price
    per category, and returns the result as a JSON response.
    """
    try:
        # The CSV file content sent from the front-end is in the 'body' of the event.
        csv_content = event['body']
        
        # Use StringIO to treat the string content as a file for Pandas to read.
        df = pd.read_csv(StringIO(csv_content))
        
        # --- Core Data Processing Logic ---
        # 1. Group the DataFrame by the 'Category' column.
        # 2. Calculate the mean (average) of the 'Price' for each group.
        # 3. Reset the index to turn the grouped output back into a DataFrame.
        summary_df = df.groupby('Category')['Price'].mean().reset_index()
        
        # Rename the 'Price' column to 'AveragePrice' for clarity in the output.
        summary_df.rename(columns={'Price': 'AveragePrice'}, inplace=True)
        
        # Convert the final DataFrame into a JSON string in a record format.
        # e.g., [{"Category": "Books", "AveragePrice": 17.5}, ...]
        summary_json = summary_df.to_json(orient='records')

        # --- Successful HTTP Response ---
        # Return a 200 OK status code with the JSON data in the body.
        return {
            'statusCode': 200,
            'headers': {
                # This 'Access-Control-Allow-Origin' header is CRUCIAL.
                # It allows your webpage (from a different domain) to call this API.
                'Access-Control-Allow-Origin': '*' 
            },
            'body': summary_json
        }

    except Exception as e:
        # If any error occurs during processing, print it to the CloudWatch logs for debugging.
        print(e)
        # Return a 500 Internal Server Error response to the front-end.
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(f"Error processing the file: {str(e)}")
        }
