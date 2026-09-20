print("가장 좋아하는 치이카와 캐릭터를 알려주세요.")
a = input()

def chooseCharacter(a):
    match a:
        case "치이카와":
            print("당신은 마음이 깊고 다정한 사람이군요!")
        case "하치와레" | "가르마":
            print("당신은 긍정적이고 성실한 사람이군요!")
        case "우사기":
            print("당신은 언제나 당당하고 재미있는 사람이군요!")
        case "모몽가":
            print("ㅠㅠ")
        case "헌책방":
            print("당신은 배려심 깊은 사람이군요!")
        case _:
            print("당신은 어른스러운 사람이군요!")

chooseCharacter(a)

print("간단한 계산기!")
num1 = int(input("첫 번째 정수를 입력하시오~~ : "))
num2 = int(input("두 번째 정수를 입력하시오~~ : "))

print(f"{num1} + {num2} = {num1 + num2}" )
print(f"{num1} - {num2} = {num1 - num2}" )
print(f"{num1} * {num2} = {num1 * num2}" )

if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}" )
else:
    print("0으로는 나눌 수 없습니당~~~")