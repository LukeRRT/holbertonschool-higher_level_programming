#!/usr/bin/pyhton3
import hidden_4

if __name__ == "__main__"":
    names = dir(hidden_4)

    for name in names:
        if x[0] == '_' and x[1] == '_':
            continue
        else:
            print(name)

