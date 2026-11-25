def parse_move(text, board):
    if text == "1":
        column = 0
    elif text == "2":
        column = 1
    elif text == "3":
        column = 2
    elif text == "4":
        column = 3
    elif text == "5":
        column = 4
    elif text == "6":
        column = 5
    elif text == "7":
        column = 6
    else:
        return None
