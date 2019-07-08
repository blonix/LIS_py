from ..utility import coreimporter
import time


class CoreLoader:
    """Load and save every core.

    Longer class information....
    Longer class information....

    Attributes:
    core_list_brain(list): list of loaded brain core classes
    core_list_sensor(list): list of loaded sensor core classes
    core_list_actuator(list): list of loaded actuator core classes
    event_queue(list): list of events
    update_rate(float): update rate of main loop as second
    """
    core_list_brain = []
    core_list_sensor = []
    core_list_actuator = []

    event_queue = []
    update_rate = 0

    def __init__(self, update_rate=0.5):
        """Initialize the class

        Args:
        update_rate(float): update rate of main loop as second
        """
        coreimporter.import_cores_from_directory("brain", self.core_list_brain)
        coreimporter.import_cores_from_directory("sensor", self.core_list_sensor)
        coreimporter.import_cores_from_directory("actuator", self.core_list_actuator)
        self.update_rate = update_rate
        self.time_now = time.time()

    def set_possible_inputs(self, variables):
        """Set possible inputs for AI

        Must be set before activating AI

        Args:
        functions: List of every function that AI can use as output

        return:
        variables: list of variables
        """
        pass

    def set_possible_outputs(self, functions):
        """Set possible outputs for AI

        Must be set before activating AI

        Args:
        functions: List of every function that AI can use as output

        return:
        bool: true on success, false on failure
        """
        pass

    def activate(self):
        """Start main loop of AI

        """
        while 1:
            for core_sensor in self.core_list_brain:

                pass
            for core_brain in self.core_list_brain:
                pass
            for core_actuator in self.core_list_brain:
                pass

            time.sleep(self.update_rate)



