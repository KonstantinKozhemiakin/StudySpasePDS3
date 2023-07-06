def read_dict(dict_name):
    with open(f"{dict_name}.txt", "r") as f:
        new_dict = {}
        lines = f.read().splitlines()
        for line in lines:
            key, value = line.split(': ')
            new_dict.update({key: value})
        return new_dict


my_d = read_dict("my_d")
print(my_d.items())
