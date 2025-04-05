message = input('Введите сообщение: ')
finish_text = ''.join(message.split())
message_length = len(finish_text)

price = 30
final_cost = message_length*price
cost_rub = final_cost // 100
cost_cent = final_cost % 100

print(f'{cost_rub} руб. {cost_cent} коп.')

# Введите сообщение: П р и в е т
# 1 руб. 80 коп.
# Введите сообщение: грузите апельсины бочках братья карамазовы
# 11 руб. 40 коп.