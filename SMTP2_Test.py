# Jungbin Choi
# I pledge to the COMP 431 Honor Code


import sys


def main():
    try:
        file_name: str = sys.argv[1]
        text_file = open(file_name, "rt")
        curr_line = ''
        next_line = text_file.readline()
        response: str = ''
        code: str = ''
        data: bool = False

        while True:
            response = ''
            curr_line = next_line
            next_line = text_file.readline()

            if (len(curr_line) >= 5) and (curr_line[0:5] == "From:"):
                sys.stderr.write("MAIL FROM: " + curr_line[6:])
                response = sys.stdin.readline()
                code = response[:3]
            elif (len(curr_line) >= 3) and (curr_line[0:3] == "To:"):
                sys.stderr.write("RCPT TO: " + curr_line[4:])
                response = sys.stdin.readline()
                code = response[:3]

                if (len(next_line) < 3) or (next_line[0:3] != "To:"):
                    sys.stderr.write(response)
                    response = ''
                    if code == "250":
                        pass
                    else:
                        data = False
                        raise EOFError()
                    sys.stderr.write("DATA\n")
                    data = True
                    response = sys.stdin.readline()
                    sys.stderr.write(response)
                    code = response[:3]
                    if code == "354":
                        pass
                    else:
                        data = False
                        raise EOFError()
                    response = ''
                    if (len(next_line) >= 5) and (next_line[0:5] == "From:"):
                        sys.stderr.write(".\n")
                        data = False
                        response = sys.stdin.readline()
                        code = response[:3]
            else:
                sys.stderr.write(curr_line)

                if (len(next_line) >= 5) and (next_line[0:5] == "From:"):
                    sys.stderr.write(".\n")
                    data = False
                    response = sys.stdin.readline()
                    code = response[:3]

            if response != '':
                sys.stderr.write(response)
                if code == "250" or code == "354":
                    pass
                else:
                    raise EOFError()

            if next_line == '':
                raise EOFError()

    except (EOFError, IndexError):
        if data:
            sys.stderr.write("\n.\n")
            response = sys.stdin.readline()
            sys.stderr.write(response[:3] + '\n')
        sys.stderr.write("QUIT\n")

    except IOError:
        return

    finally:
        text_file.close()


main()