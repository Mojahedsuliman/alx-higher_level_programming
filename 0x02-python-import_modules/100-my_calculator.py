#!usr/bin/python3
if __name__ == "__main__":
    import sys as s

    numar = len(s.argv) - 1
    if numar != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

        operator = s.argv[2]
        if operator not in "+-*/":
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

            from calculator_1 import add, sub, mul, div

            a = int(s.argv[1])
            b = int(s.argv[3])

            if operator == "+":
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif operator == "-":
                print("{} - {} = {}".format(a, b, sub(a, b)))
            elif operator == "*":
                print("{} - {} = {}".format(a, b, mul(a, b)))
            else operator == "/":
                print("{} - {} = {}".format(a, b, div(a, b)))
