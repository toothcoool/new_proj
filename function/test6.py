try:
    f = open("나 없는파일",'r')
    
except FileNotFoundError as fn:
    print("없는 파일이지롱~~")
    print(fn)
    # pass
# finally:
    # f.close()
else:
    print("오류없다")

print("pass 가 되었을까요??")