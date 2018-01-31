smiles = {'fight':"(ᕗ ͠°  ਊ ͠° )ᕗ", 'angry':"୧( ಠ Д ಠ )୨", 'ugly':"(   ͡°╭╮ʖ   ͡°)", 'dead':"ᕦ༼ ✖ ਊ ✖ ༽ᕤ", 'scared':"(∩╹□╹∩)"}


def handle_message(dir, name):
    if name in smiles:
        return(dir[name])
    else:
        return("Smile is not found")


if __name__ == "__main__":
    print("Smiles list:")
    print(*list(smiles.keys()))
    while True:
        smile_name = input("Enter necessary smile name: ")
        ans = handle_message(smiles, smile_name)

        print(ans)
