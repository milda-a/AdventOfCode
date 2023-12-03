from string import ascii_lowercase

abcs = ascii_lowercase
abc_pairs = [abcs[i] + abcs[i + 1] + abcs[i + 2] for i in range(len(abcs) - 2)]
abc_doubles = [x + x for x in abcs]
requested_passwords = 3
generated_passwords = []


def do_conversion(input_string):
    if input_string[-1] != "z":
        return input_string[:-1] + abcs[abcs.index(input_string[-1]) + 1]
    return do_conversion(input_string[:-1]) + "a"


def is_valid_password(input_string):
    if (
        any([x for x in input_string if x in "oil"])
        or not any([x for x in abc_pairs if x in input_string])
        or len([x for x in abc_doubles if x in input_string]) < 2
    ):
        return False
    global generated_passwords
    generated_passwords.append(input_string)
    return True


if __name__ == "__main__":
    password = "cqjxjnds"
    while (len(generated_passwords) != requested_passwords) or (
        not is_valid_password(password)
    ):
        print(
            (len(generated_passwords) != requested_passwords),
            (not is_valid_password(password)),
        )
        for i, x in enumerate(password):
            if x in "oil":
                password = (
                    password[0:i]
                    + abcs[abcs.index(x) + 1]
                    + "a" * (len(password) - i - 1)
                )
                break
        password = do_conversion(password)
    print(generated_passwords)
