import linecache


def get_contexts(file_path, line_number):
    try:
        return linecache.getline(file_path, line_number).strip()
    finally:
        linecache.clearcache()


def get_all_contexts(file_path) -> list:
    try:
        lines = linecache.getlines(file_path)
        lines = [i.strip() for i in lines]
        return lines
    finally:
        linecache.clearcache()


if __name__ == '__main__':
    get_all_contexts('test.txt')
