import argparse
from map.handle_map import *
from steg.handle_steg import *

parser = argparse.ArgumentParser(description="Ajout de la methode souhaiter")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-map',type=str,help="Chemin vers l'image")
group.add_argument('-steg',type=str,help="Chemin vers l'image")

args = parser.parse_args()

if args.map:
    map_print(args.map)
elif args.steg:
    reg(args.steg)
