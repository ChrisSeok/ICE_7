#9번문제. C111061 박서연

phnum_dict = dict()

while True:
    name = input('이름? ')
    
    if name == '':
        break
    
    while True:
        phnum = input('전화번호? ')
        
        if phnum != '':
            if name in phnum_dict:
                if phnum not in phnum_dict[name]:
                    phnum_dict[name].append(phnum)
            else:
                phnum_dict[name] = [phnum]
            break

print()

phnum_list = []

for phnum in phnum_dict.values():
    phnum_list.extend(phnum)

phnum_list = set(phnum_list)
print("중복되지 않는 사람 수 :", len(phnum_dict))
print("중복되지 않는 전화번호 수 :", len(phnum_list))

print()

while True:
    re_dict = {k: v for k, v in phnum_dict.items()}
    erase = input('지우고 싶은 사람의 이름 또는 전화번호를 입력하세요? ')
    
    if erase == '':
        print("검색모드로 넘어갑니다")
        break
    
    if erase in phnum_dict:
        del phnum_dict[erase]
        print("중복되지 않는 사람의 수 :", len(phnum_dict))
        print(' '.join(phnum_dict.keys()))
    
    elif erase in phnum_list:
        for name, phnum in re_dict.items():
            if erase in phnum:
                phnum.remove(erase)
            if phnum_dict[name] == []:
                del phnum_dict[name]
        phnum_list = []
        
        for phnum in phnum_dict.values():
            phnum_list.extend(phnum)
        phnum_list = set(phnum_list)
        print("중복되지 않는 전화번호의 수 :", len(phnum_list))
        print(' '.join(phnum_list))
    
    phnum_list = []
    
    for phnum in phnum_dict.values():
        phnum_list.extend(phnum)
    phnum_list = set(phnum_list)
    
while True:
    find = input('찾고 싶은 사람의 이름 또는 전화번호를 입력하세요? ')
    
    if find == '':
        print("프로그램을 종료합니다")
        break
    
    if find in phnum_dict:
        print(' '.join(phnum_dict[find]))
    
    elif find in phnum_list:
        result = []
        for name, phnum in phnum_dict.items():
            if find in phnum:
                result.append(name)
        print(' '.join(result))
    else:
        print(find, "은 등록되지 않았습니다")