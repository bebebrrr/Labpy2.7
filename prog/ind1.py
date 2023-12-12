#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"b", "f", "g", "m", "o"}  
    b = {"b", "g", "h", "l", "u"}
    c = {"e", "f", "m"}
    d = {"e", "g", "l", "p", "q", "u", "v"}

    x = (a.difference(b)).union(c.intersection(d))
    print(f"x = {x}")
    
    an = u.difference(a)
    bn = u.difference(b)

    y = (an.intersection(bn)).difference(c.union(d))
    print(f"y = {y}")
