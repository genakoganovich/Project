if __name__ == '__main__':
    il_beg = 4460
    il_end = 4780
    il_step = 80

    xl_beg = 10105
    xl_end = 10185
    xl_step = 40

    for il in range(il_beg, il_end + il_step, il_step):
        for xl in range(xl_beg, xl_end + xl_step, xl_step):
            print('{}\t{}'.format(il, xl))