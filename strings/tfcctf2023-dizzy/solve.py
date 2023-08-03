''' Embark on 'Dizzy', a carousel ride through cryptography! 
    This warmup challenge spins you around the basics of ciphers and keys. 
    Sharpen your mind, find the flag, and remember - in crypto, it's fun to get a little dizzy! '''

''' T4 l16 _36 510 _27 s26 _11 320 414 {6 }39 
    C2 T0 m28 317 y35 d31 F1 m22 g19 d38 z34 423 
    l15 329 c12 ;37 19 h13 _30 F5 t7 C3 325 z33 _21 h8 n18 132 k24 '''

input = "T4 l16 _36 510 _27 s26 _11 320 414 {6 }39 C2 T0 m28 317 y35 d31 F1 m22 g19 d38 z34 423 l15 329 c12 ;37 19 h13 _30 F5 t7 C3 325 z33 _21 h8 n18 132 k24"
result = [None]

str_list = input.split(' ')
for x in str_list:
    index = int(x[1:])
    value = x[0]
    if ( index > len(result)) :
        result.extend([None] * (index - len(result) + 1))
    result[index] = value

print(''.join(result))
