import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print('Created directory "{}"!'.format(directory))

    else:
        print('Directory "{}" exists!'.format(directory))


def create_main_data_dirs(raw_folder='raw', processed_folder='processed'):
    create_directory('../data/{}/'.format(raw_folder))
    create_directory('../data/{}/'.format(processed_folder))

def create_data_specific_folder(dataset_name='squad'):
    create_main_data_dirs(raw_folder='raw/{}'.format(dataset_name), processed_folder='processed/{}'.format(dataset_name))
