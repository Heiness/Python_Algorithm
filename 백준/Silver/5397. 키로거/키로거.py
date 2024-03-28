# 왼 [C]
# 오 [b a p]
# 오른쪽부터 pop 으로 꺼내서 왼쪽에 붙인다
# stack = [c p a b]
# 거꾸로 돌려서 [b a p c]
def test_case(input_string):
    left_stack = []
    right_stack = []
    
    for char in input_string:
        if char.isalnum():  # 알파벳 또는 숫자인 경우
            left_stack.append(char)
        elif char == '-':  # 백스페이스인 경우
            if left_stack:
                left_stack.pop()
        elif char == '<':  # 왼쪽 화살표인 경우
            if left_stack:
                right_stack.append(left_stack.pop())
        elif char == '>':  # 오른쪽 화살표인 경우
            if right_stack:
                left_stack.append(right_stack.pop())

    # 오른쪽 스택의 문자들을 왼쪽 스택으로 이동시킴
    while right_stack:
        left_stack.append(right_stack.pop())

    return ''.join(left_stack)

n = int(input())
for _ in range(n):
    input_string = input()
    print(test_case(input_string))