def get_http_error(error_code):
    status = ''
    match error_code:
        case 200:
            status = "OK"
        case 400:
            status = "Bad request"
        case 404:
            status = "Not found"
        case _:
            status = "Unknown error"
            
    return status
            

def main():
    error_code = 200
    print(get_http_error(error_code))

if __name__ == "__main__":
    main()