# Jungbin Choi
# I pledge to the COMP 431 Honor Code


import sys


# Globals
string: str = ''
value: str = ''
index: int = 0
reverse: str = ''
forward: str = []


def main():
    global string, value, index, reverse, forward
    try:
        file_name: str = sys.argv[1]
        with open(file_name, 'rt') as text_file:
            response: str = ''
            code: str = ''
            data: bool = False
            for line in text_file:
                response = ''
                if (len(line) >= 5) and (line[0:5] == "From:"):
                    if data:
                        data = False
                        sys.stderr.write(".\n")
                        response = sys.stdin.readline()
                        code = response[:3]
                        if code == "500" or code == "501" or code == "503":
                            raise EOFError()
                        sys.stderr.write(response)

                    sys.stderr.write("MAIL FROM: " + line[6:])
                    response = sys.stdin.readline()
                    code = response[:3]
                elif (len(line) >= 3) and (line[0:3] == "To:"):
                    sys.stderr.write("RCPT TO: " + line[4:])
                    response = sys.stdin.readline()
                    code = response[:3]
                else:
                    if not data:
                        data = True
                        sys.stderr.write("DATA\n")
                    sys.stderr.write(line)

                if response != '':
                    sys.stderr.write(response)
                    if code == "500" or code == "501" or code == "503":
                        raise EOFError()

    except (EOFError, IndexError):
        if data:
            sys.stderr.write(".\n")
            response = sys.stdin.readline()[:3]
            sys.stderr.write(response)
        sys.stderr.write("QUIT\n")
        return


main()