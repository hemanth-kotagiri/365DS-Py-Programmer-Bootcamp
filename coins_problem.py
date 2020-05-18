def count_heads(no_of_coins):
    # c = [0]*no_of_coins

    # for i in range(1, no_of_coins):
    #     for j in range(0, no_of_coins, i):
    #         c[j] = 1 - c[j]
    
    # return c.count(1)


    coins = ['H' for i in range(no_of_coins)]
    j = 1
    while j < no_of_coins:
        for i in range(j, no_of_coins, j+1):
            if coins[i] == 'H':
                coins[i] = 'T'
            else:
                coins[i] = 'H'
        j += 1
    
    return coins.count('H')


print(count_heads(10))