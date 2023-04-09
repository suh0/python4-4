## 함수 선언 부분 ##
def func1() :
    global a
    a=10
    print('func1()에서 a값 %d ' %a)

def func2() :
    print('func2()에서 a값 %d '%a)

## 함수 변수 선언 부분 ##
a=20

##메인 코드 부분 ##
func1()
func2()
