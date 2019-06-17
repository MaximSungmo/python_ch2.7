import mymod

def power(x, y):
    r = 1
    for i in range(y):
        r = mymod.multiply(r, x)
    return r

def main():
    print('최상의 모듈(독립실행)시, 출력 됩니다.')

if __name__ == '__main__':
    main()
else:
    print('모듈이름:' + __name__)