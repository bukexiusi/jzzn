if __name__ == "__main__":
    '''覆盖写入'''
    f = open('E:/test.txt', 'a')
    f.write('the second writing...')
    f.close()

    '''追加写入'''
    f = open('E:/test.txt', 'a')
    f.write('\nthe third writing...')
    f.close()

    '''追加写入 写入多个变量'''
    f = open('E:/test.txt', 'a')
    f.writelines(['\nthe fourth writing...', ',', 'good'])
    f.close()

    '''写入文件推荐写法'''
    with open('E:/test.txt', 'a') as f:
        f.write('\nthe third writing...')



