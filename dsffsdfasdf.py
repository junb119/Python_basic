answer = '.'

# if answer[0] == '.' :
#     answer = answer[1:] if len(answer) > 1 else '.'
if answer[-1] == '.' :
    answer = answer[:-1]
print(f'4단계 : {answer} ')
