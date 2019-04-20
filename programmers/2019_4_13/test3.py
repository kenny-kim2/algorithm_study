# 문제 설명
# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어
#
# ()() 또는 (())() 는 올바른 괄호입니다.
# )()( 또는 (()( 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때,
# 문자열 s가 올바른 괄호이면 true를 return 하고,
# 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.
#
# 제한사항
# 문자열 s의 길이 : 100,000 이하의 자연수
# 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.


def solution(s):
    s_list = list(s)
    stack = []

    for _ in range(len(s)):
        s_data = s_list.pop()
        if s_data == ')':
            stack.append(s_data)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    if len(stack) > 0:
        return False
    return True


arr1 = ['()()', ')()(', '(()(', '(())()']
return_list = [True, False, False, True]
for i in range(len(arr1)):
    if solution(arr1[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))