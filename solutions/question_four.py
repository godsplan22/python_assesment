import random

class PassGenerator:
    def __init__(self):
        pass


    def genpass(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        pw_length = 8
        mypw = ""

        for i in range(pw_length):
            next_index = random.randrange(len(alphabet))
            mypw = mypw + alphabet[next_index]

        print(mypw)



def main():

    password = int(raw_input("How strong should you password be"))

    #b = ["sosmall", "weakpass", "hmm..so weak"]
    if password <= 5:
        a = random.randint(1, 3)
        b = ["sosmall", "weakpass", "hmm..so weak", "toosmall"]
        print('Weak password.')
        print(random.choice(b))
    elif password >6:
        print('strong password.')
        dog = PassGenerator()
        dog.genpass()


if __name__ == '__main__':
            main()
