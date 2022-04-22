import os



class Preprocessing():
    """
    A class that handles the preprocessing of the raw user input
    depending on the workshop method selected
    return : json ?(str?)
    """

    def __init__(self, input_data:str):
        """
        Initializes the preprocessing class.
        :param data_dir: The directory of the data.
        :param output_dir: The directory of the output.
        """
        self.input_data:str = input_data
        self.output_data:str = None
    
    def process_hmw(self) -> str:
        """ 
        A Function that prepares usable question for GPT-3 
        for the "How might we..?" workshops
        """
         # raw input from the user interface for ex. "we, cook" > {subject},{problem}
         # output for GPT3 "How might {subjet} {problem} ?"
        problem = self.input_data
        self.output_data = f"How might we {problem}?"

        

        return self.output_data 



    def process_opposite (self) -> str:
    
        """ 
        A Function that prepares usable question for GPT-3 
        for the "Opposite thinking" workshops
        """
         # raw input from the user interface for ex. " cook" > {problem}
         # output for GPT3 "What is the opposite of how {problem} should be ?"

        pass

    def process_bad_idea(self) -> str:
    
        """ 
        A Function that prepares usable question for GPT-3 
        for the "Worst possible idea" workshops
        """
         # raw input from the user interface for ex. " cook" > {problem}
         # output for GPT3 "What is the worst possible idea about {problem} ?"
   
        pass

   