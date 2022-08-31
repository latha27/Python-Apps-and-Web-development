def group_by_owners(files):
    d = {}
    for key, value in files.items():
        if value in d:
            d[value].append(key)
        else:
            d[value] = [key]
    return d


if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))