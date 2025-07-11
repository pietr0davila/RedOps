from libraries import os, info, success_color, error, error_color, fatal, PERMISSION_DENIED, debug

def file_writer(filename, content, signature):
    try:
        data_directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        data_directory = os.path.join(data_directory_path, f"data/{signature}/")
        os.makedirs(data_directory, exist_ok=True)
        info(f"directory {data_directory} created")

        with open(f"{data_directory}/{filename}", "w") as file:
            file.write(content)
            info(f"File {data_directory} {filename} updated or created with data from {signature} content signature")

    except PermissionError: 
        error_color(f"We can't write the file, read the log for more info: {data_directory_path}/logs/RedOps.log")
        fatal(f"Can't write in file {data_directory}/{filename}. Verify permissions ant try again", PERMISSION_DENIED)
