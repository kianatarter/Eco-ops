import json

# File Reading
with open('ot7_data.json', 'r') as file:  # Replace 'your_data_file.txt' with your actual filename
    data = file.read()

# Replace single quotes with double quotes
data = data.replace("'", '"') 

# Add array brackets and convert to valid JSON string
data = f"[{data}]"  

# Load the JSON string and parse it into a Python data structure
json_data = json.loads(data)  

# Now 'json_data' should contain a list of dictionaries, ready to use!

