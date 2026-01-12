def get_http_error(error_code):
    status = {200: "OK",
              400 : "Bad request",
              404: "Not found"
              }
    
    return status.get(error_code , "Unknown error")

def main():
    error_code = 500
    print(get_http_error(error_code))

if __name__ == "__main__":
    main()