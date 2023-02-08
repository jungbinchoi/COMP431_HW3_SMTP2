# Jungbin Choi
# I pledge to the COMP 431 Honor Code


import sys


def main():
    try:
        file_name: str = sys.argv[1]
        text_file = open(file_name, "rt")
        response: str = ''
        code: str = ''
        data: bool = False
        line: str = ' '

        for line in text_file:
            response = ''

            if (len(line) >= 5) and (line[0:5] == "From:"):
                if data:
                    sys.stderr.write(".\n")
                    response = sys.stdin.readline()
                    code = response[:3]
                    data = False
                    sys.stderr.write(response)
                    if code == "250" or code == "354":
                        pass
                    else:
                        raise EOFError()

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
                if code == "250" or code == "354":
                    pass
                else:
                    raise EOFError()

    except EOFError:
        if data:
            sys.stderr.write(".\n")
            response = sys.stdin.readline()[:3]
            sys.stderr.write(response)
        sys.stderr.write("QUIT\n")
        return

    except StopIteration:
        if data:
            sys.stderr.write(".\n")
            response = sys.stdin.readline()[:3]
            sys.stderr.write(response)
        sys.stderr.write("QUIT\n")
        return

    except IOError:
        return

    finally:
        text_file.close()


main()