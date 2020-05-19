def get_train_path(num: 'int >= 0 && int <= 29999'):
    if num > 29999 | num < 0:
        print('index out of bound!')
        return 'data/mchar_train/'+'000000'+'.png'

    num_str = '{:0>6d}'.format(num) # 格式化字符串，左边补0至6位
    return 'data/mchar_train/'+num_str+'.png'

print(get_train_path(-1))