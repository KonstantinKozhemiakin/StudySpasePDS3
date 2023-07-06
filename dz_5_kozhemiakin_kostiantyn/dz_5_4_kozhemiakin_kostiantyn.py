import os


def file_catalog_count(path_=os.getcwd()):
    files = [f for f in os.listdir() if os.path.isfile(f)]
    catalog = [c for c in os.listdir() if os.path.isdir(c)]
    for c in catalog:
        print("|", c)
    for f in files:
        print(f)
    print(f"Number of directories:{len(catalog)}\nNumber of files:{len(files)}")


file_catalog_count()
