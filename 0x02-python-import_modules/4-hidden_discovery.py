#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hi
    for name in dir(hi):
        if name[0] != '__':
            print(name)
