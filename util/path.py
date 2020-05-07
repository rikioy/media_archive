import os


def app_path():
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def walk(dir):
    data = []
    if not os.path.isdir(dir):
        return None
    dirlist = os.walk(dir)
    for root, dirs, files in dirlist:
        for file in files:
            name, ext = os.path.splitext(file)
            data.append((os.path.join(root, file), name, ext))
    return data


if __name__ == '__main__':
    list = walk('c:/')
    for d in list:
        print("%s, %s, %s" % d)
    print(len(list))
