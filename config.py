from configparser import ConfigParser

# Function to read database configuration from a .ini file
def get_db_config(filename='database.ini', section='postgresql'):
    
    parser = ConfigParser()
    
    # Read the specified configuration file
    parser.read(filename)

    # Check if the section exists in the file
    if parser.has_section(section):
        # Return the section as a dictionary of parameters
        return {param: parser.get(section, param) for param in parser[section]}
    else:
        # Raise an error if the section is missing
        raise Exception(f"Section '{section}' not found in the '{filename}' file")

