def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """

    #    li = s.split(" ")
    #    li = [x[::-1] for x in li]
    #    return " ".join(li)

    return " ".join(s[::-1].split(" ")[::-1])

    # 既然要反转每个单词，不如先反转字符串，然后反转单词次序