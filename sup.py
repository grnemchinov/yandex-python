n = int(input())
b = ['щи', 'борщ', 'щавелевый_суп', 'овсяный_суп', 'суп_по-чабански']
for i in range(n):
    print(b[1 % 5])