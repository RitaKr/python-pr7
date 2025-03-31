
from app.io.input import console_input, read_file, read_file_pandas
from app.io.output import console_output, write_file

def main():
    text_from_console = console_input()
    file_content = read_file('data/example.txt')
    df_content = read_file_pandas('data/example.csv')

    console_output(text_from_console)
    console_output(file_content)
    console_output(df_content.to_string())

    write_file('data/output_console.txt', text_from_console)
    write_file('data/output_file.txt', file_content)
    write_file('data/output_df.txt', df_content.to_string())

if __name__ == "__main__":
    main()