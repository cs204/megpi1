import sm
class Turnstile(sm.SM):
    startState = 'locked'
    def getNextValues(self, state, inp):
        if state == 'locked':
            if inp == 'coin':
                return ('unloced', 'pay')
            else:
                return ('loced', 'pay')
        else:
            if inp == 'turn':
                return ('loced', 'pay')
            else:
                return ('unloced', 'enter')

if __name__ == "__main__":
    t = Turnstile()
    print(t.transduce(['turn', 'coin', 'turn', 'coin']))
