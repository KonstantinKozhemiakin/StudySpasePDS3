def conc_dict(new_dict={}, *args, **kwargs):
    new_dict.update(kwargs)
    new_dict.update(*args)
    return new_dict


dict_1 = {11: "f", 12: "dsgfg"}
dict_2 = {44: "dd"}
print(conc_dict(dict_1, dict_2, a=3, b=4))
