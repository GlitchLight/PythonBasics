# В первой строке входных данных содержится целое число n - число классов исключений. В следующих n строках содержится описание наследования классов. 
# В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. 
# Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза. 
# В следующей строке содержится число m - количество обрабатываемых исключений. Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
# Гарантируется, что никакое исключение не обрабатывается дважды.

# Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, не изменив при этом поведение программы. 
# Имена следует выводить в том же порядке, в котором они идут во входных данных.

n=int(input())
d={}
for i in range(n):
    s=input().split(' ')
    if s[0] not in d:
        d[s[0]]=[]
    ls=len(s)
    if ls==1:
        continue
    else:
        for j in range(2,ls):
            d[s[0]].append(s[j])

def search(arg):
    global end
    
    if (end==True):
        return
    
    for j in range(len(d[arg])):
        for k in exit:
            if k==d[arg][j]:
                end=True
                return
            else:
                search(d[arg][j])
        if end==True:
            return

q=int(input())
exit=[]
for i in range(q):
    s=input()
    NotFound=True
    for j in exit:
        if j==s:
            print(s)
            NotFound=False
            break
    if NotFound==True:
        end = False
        search(s)
    if end==True:
        print(s)
    exit.append(s)