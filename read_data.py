def read_in_data(file_name):
    with open(file_name, 'r') as f:
        return f.read().split('\n')
