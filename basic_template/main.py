import sys
from basic_template.mod_one.mod_one import MOD_ONE

def main():
    print((sys.argv[1:]))
    print("MAIN")
    print (MOD_ONE.func_one())
