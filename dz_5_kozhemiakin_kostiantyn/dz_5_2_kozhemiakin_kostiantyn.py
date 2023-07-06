def write_dict(my_dict, name=""):
    with open(f"{name}.txt", "w") as f:
        for key, value in my_dict.items():
            f.write(f'{key}: {value}\n')


my_d = {"first": "AAAA", "second": "BBBB"}
write_dict(my_d, "my_d")

