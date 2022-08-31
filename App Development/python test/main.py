def unique_names(names1, names2):
    for name in names1:
        names2.append(name)
    names = []
    [names.append(name) for name in names2 if name not in names]
    print(names)
if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2))