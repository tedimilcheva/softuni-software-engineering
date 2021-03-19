gifts = input().split()

gift = ''
index = ''
command = input()

while command != 'No Money':
    command_list = command.split()
    if command_list[0] == 'OutOfStock':
        gift = command_list[1]
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = 'None'
    elif command_list[0] == 'Required':
        gift = command_list[1]
        index = int(command_list[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift
    elif command_list[0] == 'JustInCase':
        gift = command_list[1]
        gifts[-1] = gift
    command = input()

to_remove = 'None'
gifts_final = [gift for gift in gifts if gift != to_remove]

gifts_line = ' '.join(gifts_final)

print(gifts_line)