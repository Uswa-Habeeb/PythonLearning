# Precedence

# BDMAS rule is applied in these statements

# Statement_1
res = 6 * 3 + 5 - 9 / 2
# 6 * 3 + 5 - 4.5
# 18 + 5 - 4.5
# 23 - 4.5
# 18.5

print(f'Result of Statement_1 = {res}')
# Result of Statement_1 = 18.5


# Statement_2
res = 6 * (3 + 5) - 9 / 2
# 6 * 8 - 9 / 2
# 6 * 8 - 4.5
# 48 - 4.5
# 43.5

print(f'Result of Statement_2 = {res}')
# Result of Statement_2 = 43.5


# Statement_3
res = 6 * 3 + 5 - (9 / 2)
# 6 * 3 + 5 - 4.5
# 18 + 5 - 4.5
# 23 - 4.5
# 18.5
# Same answer as Statement_1
# Because the operations are performed in the same order even with the brackets

print(f'Result of Statement_3 = {res}')
# Result of Statement_3 = 18.5


# Statement_4
res = 6 * 3 + (5 - 9) / 2
# 6 * 3 + -4 / 2
# 6 * 3 + -2
# 18 + -2
# 16

print(f'Result of Statement_4 = {res}')
# Result of Statement_4 = 16.0