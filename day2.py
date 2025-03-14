"""
BMI计算器

"""
height = float(input('身高(cm):'))
weight = float(input('体重（kg）:'))

bmi = weight / (height / 100) ** 2
print(f'{bmi=:.1f}')
if 18.5<=bmi <24:
    print("正常")
elif bmi<18.5:
    print("过轻")
elif bmi>=24:
    print("过重")



status_code = int(input('响应状态码:'))
match status_code:
    case 400 | 408: desc = 'Bad Request'
    case 401: desc = 'Unauthorized'
    case 403: desc = 'Forbidden'
    case 404: desc = 'Not Found'
    case 500: desc = 'Internal Server Error'
    case _: desc = 'Unknown  status Code'
print(desc)

