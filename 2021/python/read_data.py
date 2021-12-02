def read_in_data(file_name):
    with open(file_name, 'r') as f:
        read_data = f.read()
        return read_data.split('\n')
