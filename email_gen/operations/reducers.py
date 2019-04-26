def default_reader(line):
    try:
        line = line.decode('utf-8')
        line = line.replace('\x00', '')
        line = line.replace('\r\n', '')
        line = line.split('\t')
        return line
    except Exception as err:
        print(err)
        return False
