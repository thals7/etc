print("""* 나의 계산기
1. 덧셈
2. 뺄셈
3. 곱셈
4. 나눗셈
5. 종료""")
sort = input('입력 : ')
if sort == '5':
    import sys
    sys.exit()
a, b = map(int, input('숫자 2개 입력 : ').split())
if sort == '1':
    print('덧셈결과 : %d' %(a+b))
elif sort == '2':
    print('뺄셈결과 : %d' %(a-b))
elif sort == '3':
    print('곱셈결과 : %d' %(a*b))
elif sort == '4':
    print('나눗셈결과 : %d' %(a/b))