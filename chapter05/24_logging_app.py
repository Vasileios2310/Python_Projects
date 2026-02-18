import logging

def main():
    log_file = 'python.log'
    
    logger = logging.getLogger('search application')
    
    logging.basicConfig(
        level=logging.INFO,
        handlers=[logging.FileHandler(log_file, mode="a", encoding="utf-8")],
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    
    nums = [10,20,301,40,50,60]
    
    try:
        index = nums.index(30)
        print("Found!")
        print(index)
    except ValueError as e:
        logger.error(f"Error occured : {e}" , exc_info=True)


if __name__ == '__main__':
    main()
    
    