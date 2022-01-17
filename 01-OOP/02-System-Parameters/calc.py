# pylint: disable=missing-docstring


import ssl


def main():
    # We need to import argv inside the main() body to make our tests pass
    # Importing in the main function will force Python to reload argv between each tests
    from sys import argv
    operator = ['+', '*', '-']
    if(len(argv) < 3):
        print("Merci de respecter le format: [operande-1] [operator] [operande-2]")
    elif(argv[2] not in operator):
        print(f"Les operateurs valide sont: {operator}")
    else:
        return eval(f'{argv[1]} {argv[2]} {argv[3]}')
        

if __name__ == "__main__":
    print(main())
