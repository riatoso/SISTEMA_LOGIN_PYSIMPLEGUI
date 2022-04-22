import cryptocode


def criptografa(senha):
    encoded = cryptocode.encrypt(senha, "i9ti")
    return encoded


def descriptografa(csenha):
    decoded = cryptocode.decrypt(csenha, "i9ti")
    return decoded
