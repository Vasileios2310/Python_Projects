# In a function call, keyword arguments must follow positional arguments. All the keyword arguments passed must
# match one of the arguments accepted by the function (e.g. actor is not a valid argument for the parrot function),
# and their order is not important. This also includes non-optional arguments (e.g. parrot(voltage=1000) is valid
# too). No argument may receive a value more than once

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    """_summary_

    Args:
        voltage (_type_): required argument
        state (str, optional):  optional argument. Defaults to 'a stiff'.
        action (str, optional): optional argument. Defaults to 'voom'.
        type (str, optional): optional argument. Defaults to 'Norwegian Blue'.
    """
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    
parrot(1000)
print('-------------------')
parrot(voltage=1000)
print('-------------------')
parrot(action='VOOM', voltage=10)
print('-------------------')
parrot(voltage=111,action='VOOM')