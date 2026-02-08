from datetime import datetime

def log_event(event_type : str , **kwargs : dict) -> None:
    """Logs an event with a specific type and additional keyword arguments
    
    Params:
        event_type --> str 
        kwargs (dict): Additional information about the event
    """
    timestamp = datetime.now().isoformat()
    print(f"Event type : {event_type}")
    print(f"Timestamp : {timestamp}")
    
    for key , val in kwargs.items():
        print(f"{key} : {val  }")
    print("-" * 30)

def main():
    log_event("User logged in" , username = "Siberian" , status = "Success", IP = "192.168.1.180")
    log_event("File Uploades" , username = "Huskey" , status = "Failed" , Filename = "report.pdf" , reason = "404 error")

if __name__ == "__main__":
    main()