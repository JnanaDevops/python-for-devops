import sys

type_argument = sys.argv[1]

if type_argument == "t3.micro":
    print(f"'{type_argument}' can be created as free tier eligible.")
else:
    print(f"{type_argument} cannot be created")