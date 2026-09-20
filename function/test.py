def testDef(*a):
    c = ''
    for i in a:
        c += i + " "
    print(c)

testDef("치이카와", "극장판", "보세요", "꼭이요!")

def print_kwargs(**kwargs):
        """
            설명을 적어봅시다.
            파라미터가 딕셔너리로 저장되어, 딕셔너리 형태로 출력 됩니다.
        """
        print(kwargs)

print_kwargs(name='hachiware', age=5)
print(print_kwargs.__doc__)

testLambda = lambda a, b : a + b
print(testLambda(1,2))

