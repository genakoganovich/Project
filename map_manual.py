if __name__ == '__main__':
    il_beg = 4769
    il_end = 5889
    il_step = 40

    xl_beg = 10283
    xl_end = 10843
    xl_step = 40

    for il in range(il_beg, il_end + il_step, il_step):
        for xl in range(xl_beg, xl_end + xl_step, xl_step):
            print('{}\t{}'.format(il, xl))