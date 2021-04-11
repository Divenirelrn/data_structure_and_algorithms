def myPrint(val):
    print(val)

def rev_str(text, func):
    """字符串反向输出"""
    # global res

    if len(text) == 0:
        return

    rev_str(text[1:], func)
    func(text[0])