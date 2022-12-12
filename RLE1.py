# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Сжатие

data=open('In.txt','r')
text=data.read()
data.close()

print(text)
result=''
count=1

for i in range(len(text)):
    if i+1<len(text):
        if text[i+1]==text[i] and i+1<len(text):
            count+=1
        else:
            result+=f'{count}{text[i]}'
            count=1
    else:
        result += f'{count}{text[i]}'

print(result)

data_out=open('Out.txt','w')
data_out.write(result)
data.close()
