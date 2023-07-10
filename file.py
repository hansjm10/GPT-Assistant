import logging

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            data = f.read()
        return data
    except FileNotFoundError:
        logging.error(f"File '{filename}' not found.")
        return None
    except Exception as e:
        logging.error(f"Failed to read file '{filename}'. Error: {e}")
        return None
    
def write_to_file(response, filename):
    try:
        with open(filename, 'a') as f:  # 'a' for append mode
            f.write(response)
    except Exception as e:
        logging.error(f"Failed to write to file '{filename}'. Error: {e}")