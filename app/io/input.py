import pandas as pd

def console_input():
    """
    Reads input from the console

    Returns:
        str: the input read from the console
    """
    return input()

def read_file(file_path):
    """
    Reads the content of a file at the specified path

    Parameters:
        file_path (str): the path to the file to be read

    Returns:
        str: the content of the file.
    """
    with open(file_path, 'r') as file:
        return file.read()

def read_file_pandas(file_path):
    """
    Reads the content of a file at the specified path into a pandas DataFrame.

    Parameters:
        file_path (str): The path to the file to be read.

    Returns:
        pandas.DataFrame: The content of the file as a pandas DataFrame.
    """
    return pd.read_csv(file_path)