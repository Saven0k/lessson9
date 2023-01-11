import log

def read_write():
    with open('phonesbook.txt', 'r') as f:
        data = str(f"{''.join(f.read())}\n")
        log.wr2('Прочитана инфа из справочника')
    return data

def oppen():
    with open('phonesbook.txt', 'r') as f:
        data = f.read().splitlines()
        return data
