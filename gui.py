#!/usr/bin/env python3
#
#  gui.py
#  
#  Copyright 2026 johan <johan@johan-HP-Stream-Laptop-14-ds0xxx>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import sys


def main(args):
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

import tkinter as tk
from motor import run_engine
import json

def kor_motor():
    with open("match.json") as f:
        data = json.load(f)
    resultat = run_engine(data["rules"], data)
    label_result.config(text=str(resultat))

root = tk.Tk()
tk.Button(root, text="Kör motor", command=kor_motor).pack()
label_result = tk.Label(root, text="")
label_result.pack()
root.mainloop()
