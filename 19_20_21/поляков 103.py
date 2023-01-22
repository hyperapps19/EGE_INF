# СКАЧАТЬ ЗАДАЧИ: https://kpolyakov.spb.ru/download/ege1921.doc
# Задача №103 из файла

from copy import deepcopy


class Game:
    def __init__(self, k1):
        self.k1 = k1
        self.state = ('UNKNOWN', 0)
        self._move_count = 0
        self.supermove = False

    def move1(self):
        self.k1 += 2
        return self

    def move2(self):
        self.k1 *= 2
        return self

    def move3(self):
        # ничего не делаем
        self.supermove = True
        return self

    def update_state(self):
        self._move_count += 1
        if self.k1 >= 20:
            self.state = ('WIN', self._move_count)
        else:
            self.state = ('UNKNOWN', self._move_count)
        return self

    def derive_states(self):
        new_states = []
        new_states.append(deepcopy(self).move1().update_state())
        new_states.append(deepcopy(self).move2().update_state())
        if not self.supermove: new_states.append(deepcopy(self).move3().update_state())
        return new_states


def move_recursive(curr_game, moves_list, win_condition):
    states = curr_game.derive_states()

    reqs = []
    for st in states:
        if win_condition(st.state):
            reqs.append(True)
        elif len(moves_list) == 1 or st.state[0] == 'WIN':
            reqs.append(False)
        else:
            reqs.append(move_recursive(st, moves_list[1:], win_condition))
    return moves_list[0](reqs) and len(reqs) > 0


print('19. ', end='')
for S in range(1, 19 + 1):
    if move_recursive(Game(S), [any, any], lambda x: x == ('WIN', 2)):
        print(S)
        break

print('20. ', end='')
for S in range(1, 19 + 1):
    if move_recursive(Game(S), [any], lambda x: x == ('WIN', 1)):
        continue
    if move_recursive(Game(S), [any, all, any], lambda x: x == ('WIN', 3)):
        print(S, end=' ')
print()
s_vals = []
print('21. ', end='')
for S in range(1, 19 + 1):
    if move_recursive(Game(S), [all, any] * 1000, lambda x: x[0] == 'WIN' and x[1] % 2 == 0):
        s_vals.append(S)

print(min(s_vals), max(s_vals))
