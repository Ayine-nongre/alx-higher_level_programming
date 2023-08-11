#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as names

    for i in dir(names):
        if i[0] != "_" and i[1] != "_":
            print(i)
