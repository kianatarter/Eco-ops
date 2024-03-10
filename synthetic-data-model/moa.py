import json

# ... (load your data into a variable called 'data') 


# Replace single quotes with double quotes
data = data.replace("'", '"') 

# Add array brackets and convert to valid JSON string
data = f"[{data}]"  

# Load the JSON string and parse it into a Python data structure
json_data = json.loads(data)  

# Now 'json_data' should contain a list of dictionaries, ready to use!

