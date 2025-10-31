names = [
    "김형규 (20200369)",
    "이진철 (2025111768)",
    "김하린 (2025115192)",
    "변정수 (2025111423)"
]

name = input("삭제할 이름을 입력하세요: ")

if name in names:
    names.remove(name)
    print(f"{name} 님의 이름이 삭제되었습니다!")
else:
    print("해당 이름이 목록에 없습니다.")

print("\n[현재 남은 명단]")
for n in names:
    print("-", n)
