import os
import openai


class Generator():
    """
    A Class that generate idea for user based GPT-3 API.
    """
    def __init__(self, question:str, number_of_idea: int, workshop_method:str, enhaced:bool = False) -> None:
        """
        A constructor function for Generator class.
        :param question: A question that user want to ask.
        :param number_of_idea: Number of idea that user want to get.
        :param enhaced: A boolean value that indicate if user want to get enhaced idea or not.
        :param workshop_method: A string value that indicate which workshop method user want to use.
        """
        self.question:str = question
        self.number_of_idea:int = number_of_idea
        self.enhaced:bool = enhaced
        self.workshop_method:str = workshop_method
        self.idea_list:list = []
        self.idea_list_enhaced:list = []
        self.api_key:str = os.getenv('OPENAI_API_KEY')

    def connect_openai(self) -> bool:
        """
        A function that create api connection.
        :return: A boolean value that indicate if api connection is created or not.
        """
        try:
            openai.api_key = self.api_key
        except openai.exceptions.InvalidAPIKeyError:
            return False
        else:
            return True
        


    def generate_idea(self) -> bool:
        """
        A Funtion that generate idea for user based GPT-3 API.
        :return: None
        """
        if self.connect_openai():
            """
            If api connection is created, then generate idea.
            """
            if self.enhaced:
                """
                If user want to get enhaced idea, then generate idea with enhaced parameter.
                """
                # @TODO: Add a try catch block for this function. @gio
            else:
                """
                If user want to get normal idea, then generate idea with normal parameter.
                """

                # @TODO: Add a try catch block for this function. @gio
        else:
            pass


        