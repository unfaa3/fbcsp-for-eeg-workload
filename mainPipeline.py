from bin.MLEngine import MLEngine

if __name__ == "__main__":
    '''Example for loading Korea University Dataset'''
    # dataset_details = {
    #     'data_path': "/Volumes/Transcend/BCI/KU_Dataset/BCI dataset/DB_mat",
    #     'subject_id': 1,
    #     'sessions': [1],
    #     'ntimes': 1,
    #     'kfold': 10,
    #     'm_filters': 2,
    # }

    '''Example for loading BCI Competition IV Dataset 2a'''
    # dataset_details={
    #     'data_path' : "D:/2023/py_bath/BCI/data_set/BCICIV_2a_gdf",
    #     'file_to_load': 'A01T.gdf',
    #     'ntimes': 1,
    #     'kfold':10,
    #     'm_filters':2,
    #     'window_details':{'tmin':0.5,'tmax':2.5}
    # }
    #
    # ML_experiment = MLEngine(**dataset_details)
    # ML_experiment.experiment()

    '''CSP'''
    # dataset_details={
    #     'data_path' : "D:/2023/py_bath/BCI/data_set/BCICIV_2a_gdf",
    #     'file_to_load': 'A01T.gdf',
    #     'ntimes': 1,
    #     'kfold':10,
    #     'm_filters':2,
    #     'window_details':{'tmin':0.5,'tmax':2.5}
    # }

    # dataset_details = {
    #     'data_path': "D:/2023/py_bath/BCI/2021_code/SIDdataset",
    #     'subject_id': 1,
    #     'sessions': [1],
    #     'file_to_load': 'dataset.mat',
    #     'ntimes': 1,
    #     'kfold': 10,
    #     'm_filters': 2,
    #     # 'window_details': {'tmin': 0.5, 'tmax': 2.5}
    # }

    dataset_details = {
        'data_path': "D:/2023/py_bath/workload/my_code/stew",
        'subject_id': 1,
        'sessions': [1],
        'file_to_load': 'stew_dataset.mat',
        'ntimes': 1,
        'kfold': 10,
        'm_filters': 2,
        # 'window_details': {'tmin': 0.5, 'tmax': 2.5}
    }

    ML_experiment = MLEngine(**dataset_details)
    ML_experiment.experiment()
