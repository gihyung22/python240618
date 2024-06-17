t=(1,2,3)
type(t)


#Tuple 형식
tp = ("아이폰", "아이패드","갤럿기")
print(len(tp))
print(tp[0])
print(tp.index("아이패드"))

def times(a,b):
    return a+b,a*b

print(times(3,4))

print("id: %s, name: %s" % ("kim", "김유신"))

#형식변환
a= list((1,2,3))
print(a)
b=set(a)
print(b)

#딕셔너리
color={"apple":"red", "banana":"yellow"}
print(color["apple"])
print(len(color))
color["cherry"]="red"
print(color)
del color["apple"]
print(color)

for item in color.item():
    print(item)

for 