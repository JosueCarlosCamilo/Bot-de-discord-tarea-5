import random 

def gen_pass(long):

    caract = "+-/*!&$#?=@abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    psw_generada = ''
    for i in range(long):
        psw_generada += random.choice(caract)
    
    return psw_generada

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)

def flip_coin():
    flip = random.randint(0, 2)             
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"

