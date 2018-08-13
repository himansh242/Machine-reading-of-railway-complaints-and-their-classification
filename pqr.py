def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    if index==0 and s[index+len(char)+1]=='_'
                    return 1;
                    if s[index-1]=='_' and s[index+len(char)+1]=='_'
                    return 1;
            index += 1
    return -1
