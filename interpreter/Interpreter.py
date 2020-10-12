from pyparsing import Word, OneOrMore, Optional, Group, Suppress, alphanums

from interpreter.Aircondition import Aircondition
from interpreter.Boiler import Boiler
from interpreter.Fridge import Fridge
from interpreter.Garage import Garage
from interpreter.Gate import Gate
from interpreter.Heating import Heating


def main():
    word = Word(alphanums)
    command = Group(OneOrMore(word))
    token = Suppress("->")
    device = Group(OneOrMore(word))
    argument = Group(OneOrMore(word))
    event = command + token + device + Optional(token + argument)
    gate = Gate()
    garage = Garage()
    airco = Aircondition()
    heating = Heating()
    boiler = Boiler()
    fridge = Fridge()

    open_actions = {'gate': gate.open,
                    'garage': garage.open,
                    'air condition': airco.turn_on,
                    'heating': heating.turn_on,
                    'boiler temperature': boiler.increase_temperature,
                    'fridge temperature': fridge.increase_temperature}
    close_actions = {'gate': gate.close,
                     'garage': garage.close,
                     'air condition': airco.turn_off,
                     'heating': heating.turn_off,
                     'boiler temperature': boiler.decrease_temperature,
                     'fridge temperature': fridge.decrease_temperature}

    tests = ('open -> gate',
             'close -> garage',
             'turn on -> air condition',
             'turn off -> heating',
             'increase -> boiler temperature -> 5 degrees',
             'decrease -> fridge temperature -> 2 degrees')

    while True:

        print(' 1. gate |==| 2. garage |==| 3. air condition |==| 4. heating |==| 5. boiler |==| 6.fridge |==| 7.exit')
        key = input('Choose object: ')
        if key == '1':
            option = input('Choose option: 1 - open, 2 - close: ')
            if option == '1':
                open_actions['gate']()
            elif option == '2':
                close_actions['gate']()
        elif key == '2':
            option = input('Choose option: 1 - open, 2 - close: ')
            if option == '1':
                open_actions['garage']()
            elif option == '2':
                close_actions['garage']()
        elif key == '3':
            option = input('Choose option: 1 - turn on, 2 - turn off: ')
            if option == '1':
                open_actions['air condition']()
            elif option == '2':
                close_actions['air condition']()
        elif key == '4':
            option = input('Choose option: 1 - turn on, 2 - turn off: ')
            if option == '1':
                open_actions['heating']()
            elif option == '2':
                close_actions['heating']()
        elif key == '5':
            option = input('Choose option: 1 - increase, 2 - decrease: ')
            if option == '1':
                t = int(input('Insert amount of temperature difference: '))
                open_actions['boiler temperature'](t)
            elif option == '2':
                t = int(input('Insert amount of temperature difference: '))
                close_actions['boiler temperature'](t)
        elif key == '6':
            option = input('Choose option: 1 - increase, 2 - decrease: ')
            if option == '1':
                t = int(input('Insert amount of temperature difference: '))
                open_actions['fridge temperature'](t)
            elif option == '2':
                t = int(input('Insert amount of temperature difference: '))
                close_actions['fridge temperature'](t)
        elif key == '7':
            exit()
        else:
            print(f'unknown option: {key}')

#ZADANIE NR 1 - PONIŻEJ ROZWIĄZANIE (nieprawidłowy argument)

    # for t in tests:
    #     if len(event.parseString(t)) == 2:  # no argument
    #         cmd, dev = event.parseString(t)
    #         cmd_str, dev_str = ' '.join(cmd), ' '.join(dev)
    #         if 'open' in cmd_str or 'turn on' in cmd_str:
    #             open_actions[dev_str]()
    #         elif 'close' in cmd_str or 'turn off' in cmd_str:
    #             close_actions[dev_str]()
    #     elif len(event.parseString(t)) == 3:  # argument
    #         cmd, dev, arg = event.parseString(t)
    #         cmd_str = ' '.join(cmd)
    #         dev_str = ' '.join(dev)
    #         arg_str = ' '.join(arg)  ############ poprawiony błąd zadanie nr 1
    #         num_arg = 0
    #         try:
    #             # extract the numeric part
    #             num_arg = int(arg_str.split()[0])
    #         except ValueError as err:
    #             print(f"expected number but got: '{arg_str[0]}'")
    #         if 'increase' in cmd_str and num_arg > 0:
    #             open_actions[dev_str](num_arg)
    #         elif 'decrease' in cmd_str and num_arg > 0:
    #             close_actions[dev_str](num_arg)


if __name__ == '__main__':
    main()
