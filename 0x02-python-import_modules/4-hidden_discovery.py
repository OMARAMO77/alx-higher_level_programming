#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    n = len(names)
    for a in range(n):
        if names[a][:2] != "__":
            print(names[a])
