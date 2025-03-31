def console_output(text):
    """
    Outputs the given text to the console

    Parameters:
        text (str): the text to be output to the console.
    """
    print(text)

def write_file(file_path, text):
    """
    Writes the given text to a file at the specified path

    Parameters:
        file_path (str): the path to the file where the text will be written
        text (str): the text to be written to the file
    """
    with open(file_path, 'w') as file:
        file.write(text)