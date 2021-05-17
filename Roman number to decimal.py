from rom import rom_generate

while True:
    num = int(input('enter your number to convert in Roman number'))
    print((rom_generate(num)))
    i = input("If you want to check again type yes")
    if i == 'y':
        continue
    else:
        break
