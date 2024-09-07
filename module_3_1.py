def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    str_ = str(string)
    cartege = (len(str_), str_.upper(), str_.lower())
    return cartege

def is_contains(string, list_to_search ):
    count_calls()
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() == string.lower():
            overlap = True
            break
        else:
            overlap = False
            continue
    return overlap

calls = 0
print(string_info('Vilage'))
print(string_info('kaleidoscope'))
print(string_info('Pilot'))
print(string_info('Сockatoo'))
print(is_contains('Smile', ['mile', 'StIle', 'smILE','sMiTe', 'smIKe', 'StikE'])) # Smile ~ smILE
print(is_contains('driver', ['drive', 'river', 'rider', 'strider'])) # No matches
print(is_contains('Monitor', ['Tor', 'MoneY', '','motor'])) # No matches
print(is_contains('argument', ['orator', 'aRt', 'studenT', 'ArGuMent']))
print(calls)

