def find_it(seq):
    seq_dict = dict.fromkeys(seq, 0)

    for i in seq:
        seq_dict[i] += 1

    for key, value in seq_dict.items():
        if value % 2 != 0:
            return key
