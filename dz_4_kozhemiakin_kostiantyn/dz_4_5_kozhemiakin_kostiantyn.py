def moda_alpha(my_string):
    alpha_string = [i for i in my_string if i.isalpha()]
    unique_alpha = list(set(alpha_string))
    moda_symb = ""
    moda_count = 0
    for j in range(len(unique_alpha)):
        symb_count = alpha_string.count(unique_alpha[j])
        if symb_count > moda_count:
            moda_symb = unique_alpha[j]
            moda_count = symb_count
        elif symb_count == moda_count:
            moda_symb += unique_alpha[j]
    return moda_symb


print(moda_alpha("qqqqqqwwwwwwwwwwwerrrrrrrrrrrrrrty"))