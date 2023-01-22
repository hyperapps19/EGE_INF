# СКАЧАТЬ ЗАДАЧИ: https://kpolyakov.spb.ru/download/ege1921.doc
# Задача №102 из файла

from copy import deepcopy


class Game:
    def __init__(self, knabor):
        self.karta = -1
        self.kart_nabor = deepcopy(knabor)
        self.state = ('UNKNOWN', 0)
        self._move_count = 0

    def add_karta(self, karta):
        self.karta = karta
        self.kart_nabor[karta] -= 1
        if self.kart_nabor[karta] == 0:
            del self.kart_nabor[karta]
        return self

    def update_state(self):
        self._move_count += 1
        if len(self.derive_states()) == 0:
            self.state = ('WIN', self._move_count)
        else:
            self.state = ('UNKNOWN', self._move_count)
        return self

    def derive_states(self):
        new_states = []
        for vv in self.kart_nabor:
            if (vv == self.karta or vv == self.karta + 1 or self.karta == -1) and self.kart_nabor[vv] >= 1:
                new_states.append(deepcopy(self).add_karta(vv).update_state())
        return new_states


def move_recursive(curr_game, moves_list, win_condition, do_print=True):
    states = curr_game.derive_states()
    reqs = []
    for st in states:
        if win_condition(st.state):
            reqs.append(True)
        elif len(moves_list) == 1 or st.state[0] == 'WIN':
            reqs.append(False)
        else:
            reqs.append(move_recursive(st, moves_list[1:], win_condition))
    if len(moves_list) == 1000 * 2 and do_print:
        print([sta.karta for sta in states], reqs)
    return moves_list[0](reqs) and len(reqs) > 0


# с каких карт начинает - где True
move_recursive(Game({7: 1, 8: 3, 9: 2}), [any, all] * 1000, lambda x: x[0] == 'WIN' and x[1] % 2 == 1)
move_recursive(Game({5: 1, 6: 2, 7: 3, 8: 1, 9: 3, 10: 2}), [any, all] * 1000, lambda x: x[0] == 'WIN' and x[1] % 2 == 1)

count = 0
for a in [1, 2, 3, 4]:
    for b in [1, 2, 3, 4]:
        for c in [1, 2, 3, 4]:
            for d in [1, 2, 3, 4]:
                if move_recursive(Game({4: a, 5: b, 6: c, 7: d}), [all, any] * 1000, lambda x: x[0] == 'WIN' and x[1] % 2 == 0, do_print=False):
                    count += 1
print(count)

