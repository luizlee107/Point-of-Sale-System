
a=[]
b=' '
while b != 'N':
    num=int(input('Digit a number: '))
    if num not in a:
        a.append(num)
    else:
        print('The number is duplicate.I wil not add the value.')
         
    b=input('Do u want to continue:[Y/N] ').upper().strip()[0]
    while b not in 'YN':
        b=input('Do u want to continue:[Y/N] ').upper().strip()[0]   

a.sort()

print(f'You type the follow values: {a}')