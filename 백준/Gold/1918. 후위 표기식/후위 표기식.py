def main():
    formula = list(input())
    stack = [] # 연산자, 괄호가 담길 스택
    answer = ''

    for tmp in formula:
        if tmp.isalpha(): # 문자는 바로 정답 문자열에 추가
            answer += tmp
        elif tmp == '(': # 여는 괄호는 스택에 추가
            stack.append(tmp)
        elif tmp == '*' or tmp == '/': # 곱셈/나눗셈은 묶여 있음
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(tmp)
        elif tmp == '+' or tmp == '-': # 덧셈/뺄셈은 괄호만 아니면 덜어내기
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(tmp)
        else: # 닫는 괄호는 여는 괄호 전까지 다 정답으로 추가
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop() # 여는 괄호 제거

    while stack: # 남아 있는 문자 정답으로 추가하기
        answer += stack.pop()
    print(answer)

if __name__ == '__main__':
    main()