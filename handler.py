smiles = {'smile_name_1':"smile_1", 'smile_name_2':"smile_2", 'smile_name_3':"smile_3", 'smile_name_4':"smile_4", 'smile_name_5':"smile_5"}


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