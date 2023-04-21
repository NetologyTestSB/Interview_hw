
class Stack(list):

    def isEmpty(self):
        return len(self) == 0

    def push(self, item):
        self.append(item)

    def pop(self):
        if len(self) > 0:
            item = self[-1]
            self.__delitem__(-1)
            return item

    def peek(self):
        if len(self) > 0:
            item = self[-1]
            return item

    def size(self):
        return len(self)


def check_brackets_ok(input_str: str) -> bool:
    match_dict = {'(': ')', '[': ']', '{': '}'}
    loc_stack = Stack()
    for sym in input_str:
        if sym in ['(', ')', '[', ']', '{', '}']:
            if sym in match_dict:
                loc_stack.push(sym)
            else:
                if sym == match_dict.get(loc_stack.peek()):
                    loc_stack.pop()
                else:
                    return False
    return loc_stack.isEmpty()

def self_test():
    test_list =['}{}', '2{{[(])]}}', '[[{())}]', '[([])((([[[]]])))]{()}', '(((([{}]))))', '']
    expected_list = [False, False, False, True, True, True]
    error_list = []
    for ind, test_str in enumerate(test_list):
        if check_brackets_ok(test_str) != expected_list[ind]:
            error_list.append(ind)
    if error_list:
        print('ошибки теста для строк: ', *error_list)
    else:
        print('тест выполнен успешно')

def check_brackets(input_str: str):
    print('Сбалансировано' if check_brackets_ok(input_str) else 'Несбалансировано')


def main():
    while True:
        print(f'{"=" * 22}\nq - выход из программы\nВведите команду или строку со скобками: ')
        inp_str = input()
        if inp_str == 'q':
            return
        else:
            check_brackets(inp_str)


if __name__ == '__main__':
    self_test()

    main()

