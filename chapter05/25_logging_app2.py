import logging
from typing import List , Any


def configure_logger(log_file : str , logger_name : str) -> logging.Logger:
    """
        Configure and return a logger with both file and console handlers.
        
        Args:
          log_file(str) : the name of the log file,
          logger_name(str) : the name of the logger
          
        Returns:
            loggeng.Logger : Configures logger instance 
    """
    
    # create a logger
    my_logger = logging.getLogger(logger_name)
    my_logger.setLevel(logging.INFO)
    
    # file handler
    file_handler = logging.FileHandler(log_file , mode='a')
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s%(levelname)s%(name)s%(message)s")
    )
    
    # console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
         logging.Formatter("%(asctime)s%(levelname)s%(name)s%(message)s")
    )
    
    # add handlers to the logger
    
    my_logger.addHandler(file_handler)
    my_logger.addFilter(console_handler)
    
    return my_logger

def search_item(items : List[Any] , item_to_find : Any , logger : logging.Logger) -> int:
    """
    Search for an item in a List and returns its index
    
    Args:
        items (List[Any]) : List of items to search within
        item_to_find(Any) : the item to find
        logger (logging.LOgger) : Logger instance for logging messages.
        
    Returns:
        int : the index of the item in the list
        
    Raises:
        ValueError : if the item is not found
    """  
    
    if not items:
        logging.warning("The list is empty.")
        raise ValueError("Can not search in an empty List")
    
    try:
        index = items.index(item_to_find)
        logger.info(f"Item {item_to_find} found on index : {index}")
        return index
    except ValueError as ex:
        logger.error(f"Item {item_to_find} not found in the List. Error {ex}")
        raise # Re-raise the same ValueError

def main():
    log_file = 'python.log'
    
    logger = configure_logger(log_file , 'search')
    
    employees_names = ["Alice" , "Bob" , "Charlie" , "Diana" , "Eve"]
    employees_to_find = "Alice"
    
    try:
        index = search_item(employees_names , employees_to_find , logger)
        print(f"Employee '{employees_to_find}' found on index : {index}")
    except ValueError:
        print(f"Employee '{employees_to_find}' not found on List")
    
    
if __name__ == "__main__":
    main()   
        