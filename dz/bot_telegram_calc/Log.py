def wr2(data):
    with open('logger.txt', 'a') as f:
        f.write(f'{data}\n')
def wr(data):
    with open('logger.txt', 'w') as f:
        f.write(f'{data}\n')