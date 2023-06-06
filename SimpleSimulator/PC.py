from CONVERTME import int_to_bin, bin_to_int, bin_to_dec_IF, findIEEE_FI

class pc:

    def __init__(self):
        self.pc = 0

    def update(self, new_pc):
        self.pc = new_pc

    def dump(self):
        pc_bin = int_to_bin(self.pc)
        pc_bin = pc_bin.zfill(7)
        print(pc_bin, end='        ')
    
    