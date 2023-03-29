import pandas as pd
import json
import io
import os


# ------ CSV ------

def load_csv(path, index='none', index_names=None):
    """
    Loads a csv file as pandas dataframe
    :param path: relativer Pfad inklusive Dateiname und -endung
    :param index: Die Spalte, die als Index genutzt werden soll
    :param index_names:
    :return: pandas dataframe
    """
    if index_names is None:
        index_names = [None]
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    dataframe = pd.read_csv(path)
    if index != 'none':
        dataframe.set_index(index, inplace=True)
        dataframe.index.names = index_names
    return dataframe


def save_csv(data, path):
    """
    speichert einen pandas dataframe als .csv Datei ab
    :param data: pandas dataframe
    :param path: relativer Pfad inklusive Dateiname und -endung
    """
    __write_to_file(data, path, 'csv')


def __to_csv(data, path):
    data.to_csv(path)
    print("Wrote csv data to file")


# ------ JSON ------

def load_json(path):
    """
    Lädt ein JSON-Objekt aus einer .json Datei
    :param path: relativer Pfad inklusive Dateiname und -endung
    :return: JSON-Objekt (Dictionary)
    """
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_json(data, path):
    """
    Speichert eine Datenstruktur als JSON
    :param data: Die Datenstruktur, die gespeichert werden soll
    :param path: relativer Pfad inklusive Dateiname und -endung
    """
    __write_to_file(data, path, 'json')


def __to_json(data, outfile, existing=False):
    if existing:
        json.dump(data, outfile, indent=2)
        print("Wrote json to file")
    else:
        outfile.write(json.dumps(data, indent=2))
        print("Created json file and wrote data")


# ------ General ------

def __write_to_file(data, path, file_type):
    if os.path.exists(path) and os.access(path, os.R_OK):
        with open(path, 'w') as outfile:
            match file_type:
                case 'json':
                    __to_json(data, outfile, existing=True)
                case 'csv':
                    __to_csv(data, outfile)
    else:
        with io.open(os.path.join(path), 'w') as outfile:
            match file_type:
                case 'json':
                    __to_json(data, outfile, existing=False)
                case 'csv':
                    __to_csv(data, outfile)
