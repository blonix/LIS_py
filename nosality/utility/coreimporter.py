# import importlib
import os
import sys


def import_cores_from_directory(path, core_list):
    """Dynamically import every cores from given path and append to the given list

    Args:
    path (string): path of brain/actuator/sensor core directory
    core_list (list): imported classes will be saved in this list.

    Returns:
    int: number of loaded cores
    """
    cores = []
    for directory in os.listdir(path):
        if os.path.isdir(directory):
            cores.append(directory)

    core_count = 0
    if len(cores) != 0:
        for core in cores:
            if is_valid_core(path + "/" + core):
                try:
                    module = __import__(path + "/" + core + "/" + core)
                    class_name = getattr(module, "class_name")
                    core_class = getattr(module, class_name)
                    new_instance = core_class()
                    core_list.append(new_instance)
                    core_count += 1
                except ImportError:
                    print("ERROR : fail Importing core : " + core + " : " + sys.exc_info()[0])
    else:
        print("ERROR : no core in " + path)

    return core_count


def is_valid_core(path):
    """

    :param path:
    :return:
    """
    return True

