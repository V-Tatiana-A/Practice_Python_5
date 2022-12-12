# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Восстановление

data=open('Out.txt','r')
text=data.read()
data.close()

print(text)

result=''
i=0

while i in range(len(text)):
    if text[i].isdigit():
        num=int(text[i])
        while (text[i + 1].isdigit()):
            num=int(f'{num}{text[i+1]}')
            i += 1
        i+=1
    else:
        for j in range (1,num+1):
            result+=text[i]
        i+=1

print(result)