def decrypt_message(message : str) -> str:
    """
    Decrypts a message by removing all numeric characters.
    Args:
        message(str): The encrypted ,essage containing characters
    
    Returns:
        str: The encrypted message
    """
    decrypt_message = ""
    for char in message:
        if not char.isnumeric():
            decrypt_message += char
    return decrypt_message
    
def main() -> None:
    strange_message = "123H222E5677L43L22O 3W22O44R99L8886D7654"
    
    decrypted_message = decrypt_message(strange_message)
    print(decrypted_message)
    
if __name__ == "__main__":
    main()