smiles = {'fight': "(ᕗ ͠°  ਊ ͠° )ᕗ", 'angry': "୧( ಠ Д ಠ )୨", 'ugly': "(   ͡°╭╮ʖ   ͡°)", 'dead': "ᕦ༼ ✖ ਊ ✖ ༽ᕤ", 'scared': "(∩╹□╹∩)"}
smiles_pop = {'fight': 0, 'angry': 0, 'ugly': 0, 'dead': 0, 'scared': 0}


def handle_message(dir_1, name, dir_2):
    if name in smiles:
        dir_2[name] += 1
        return dir_1[name]
    elif name == "Most popular":
        max_used = -1
        for i in dir_2:
            if dir_2[i] > max_used:
                max_used = dir_2[i]
                smile = i
        return smile
    else:
        return "Smile is not found"


if __name__ == "__main__":
    print("Smiles list:")
    print(*smiles.keys())
    while True:
        smile_name = input("Enter necessary smile name: ")
        ans = handle_message(smiles, smile_name, smiles_pop)

        print(ans)
