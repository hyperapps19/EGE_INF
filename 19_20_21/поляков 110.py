# СКАЧАТЬ ЗАДАЧИ: https://kpolyakov.spb.ru/download/ege1921.doc
# Задача №110 из файла

from copy import deepcopy


class Game:
    def __init__(self, k1):
        self.k1 = k1
        self.state = ('UNKNOWN', 0)
        self._move_count = 0
        self.prev_xod_DEL2 = -1
        self.prev_xod_NEDEL2 = -1

    def move1(self):
        self.k1 += 2
        if self._move_count % 2 == 0:
            self.prev_xod_DEL2 = 1
        else:
            self.prev_xod_NEDEL2 = 1
        return self

    def move2(self):
        self.k1 += 5
        if self._move_count % 2 == 0:
            self.prev_xod_DEL2 = 2
        else:
            self.prev_xod_NEDEL2 = 2
        return self

    def move3(self):
        self.k1 += 12
        if self._move_count % 2 == 0:
            self.prev_xod_DEL2 = 3
        else:
            self.prev_xod_NEDEL2 = 3
        return self

    def move4(self):
        self.k1 *= 2
        if self._move_count % 2 == 0:
            self.prev_xod_DEL2 = 4
        else:
            self.prev_xod_NEDEL2 = 4
        return self

    def update_state(self):
        self._move_count += 1
        if self.k1 >= 121:
            self.state = ('WIN', self._move_count)
        else:
            self.state = ('UNKNOWN', self._move_count)
        return self

    def derive_states(self):
        new_states = []
        if self._move_count % 2 == 0:
            if self.prev_xod_DEL2 != 1:
                new_states.append(deepcopy(self).move1().update_state())
            if self.prev_xod_DEL2 != 2:
                new_states.append(deepcopy(self).move2().update_state())
            if self.prev_xod_DEL2 != 3:
                new_states.append(deepcopy(self).move3().update_state())
            if self.prev_xod_DEL2 != 4:
                new_states.append(deepcopy(self).move4().update_state())
        else:
            if self.prev_xod_NEDEL2 != 1:
                new_states.append(deepcopy(self).move1().update_state())
            if self.prev_xod_NEDEL2 != 2:
                new_states.append(deepcopy(self).move2().update_state())
            if self.prev_xod_NEDEL2 != 3:
                new_states.append(deepcopy(self).move3().update_state())
            if self.prev_xod_NEDEL2 != 4:
                new_states.append(deepcopy(self).move4().update_state())
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
for S in range(1, 121):
    if move_recursive(Game(S), [any, any], lambda x: x == ('WIN', 2)):
        print(S)
        break


print('20. ', end='')
for S in range(1, 121):
    if move_recursive(Game(S), [any], lambda x: x == ('WIN', 1)):
        continue

    if move_recursive(Game(S), [any, all, any], lambda x: x == ('WIN', 3)):
        print(S)
        break

print('21. ', end='')
s_vals = []
for S in range(1, 121):
    if move_recursive(Game(S), [all, any, all, any], lambda x: x == ('WIN', 2) or x == ('WIN', 4)):
        continue
    # "позволяющая ему выиграть, по крайней мере, своим третьим ходом" == первым ИЛИ вторым ИЛИ третьим
    if move_recursive(Game(S), [all, any, all, any, all, any], lambda x: x[0] == 'WIN' and x[1] % 2 == 0):
        s_vals.append(S)
print(min(s_vals), max(s_vals))
