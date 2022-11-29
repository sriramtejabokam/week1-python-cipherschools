#class59&60:
t = input()
temp_var = ""
i = 0
while i<len(t):
    if t[i] not in temp_var:
        temp_var += t[i]
        print(f"{t[i]} : {t.count(t[i])}")
        i +=1