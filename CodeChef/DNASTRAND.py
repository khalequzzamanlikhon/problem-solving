while True:
  try:
    for _ in range(int(input())):
        x = int(input())
        s = input()[:x]
        s_list = list(s)
        for i in range(len(s)):
            if s_list[i] == 'A':
                s_list[i] = 'T'
            elif s_list[i] == 'T':
                s_list[i] = 'A'
            elif s_list[i] == 'C':
                s_list[i] = 'G'
            elif s_list[i] == 'G':
                s_list[i] = 'C'
        result = ""
        for i in range(len(s_list)):
            result += s_list[i]
        print(result)
  except:
    break