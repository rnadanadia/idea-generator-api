import os



class Preprocessing():
    """
    A class that handles the preprocessing of the data.
    """

    def __init__(self, input_data:str):
        """
        Initializes the preprocessing class.
        :param data_dir: The directory of the data.
        :param output_dir: The directory of the output.
        """
        self.input_data:str = input_data
        self.output_data:str = None
    
    def prepare_question(self) -> bool:
        """
        A Function that prepares usable question for GPT-3.
        :return: The string that contains prepared output.
        """

        pass

    def prepare_answer(self) -> bool:
        """
        A Function that prepares usable answer for API.
        :return: The string that contains prepared output.
        """

        pass
        

   