class Valida:
    def v_cpf(self, cpf):
        for i in cpf:
            try:
                i = int(i)
                continue
            except:
                return 0
        cpf = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
        return cpf

    def v_telefone(self, telefone):
        for i in telefone:
            try:
                i = int(i)
                continue
            except:
                return 0
        telefone = f"({telefone[0:2]}){telefone[2:7]}.{telefone[7:11]}"
        return telefone


