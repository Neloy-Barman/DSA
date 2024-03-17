
def recursionReverseString(s: list[str]) -> list[str]:
    if len(s) == 1:
        return s[0]
    return s[-1]+recursionReverseString(s[0:len(s)-1])


def main():
    s = recursionReverseString(['s','t','r','i','n','g'])
    print(s)

if __name__ == "__main__":
    main()