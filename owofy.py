def owofunction(cutiemessage):
    text = []
    text = list(str(cutiemessage))
    #iterate through a string by its index values
    #the text will be modified by changing r's and l's to w
    for idx, val in enumerate(text):
            if val == 'r':
                text[idx] = 'w'
            elif val == 'l':
                text[idx] = 'w'
    #sent back to the main function so it can be sent by the bot on discord
    return text
