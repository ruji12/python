# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.


accounts=[[1,2,3],[3,4,5],[7,8,9]]
maximum_wealth = 0


for account in accounts:
    total_sum = sum(account)
    maximum_wealth= max(maximum_wealth,total_sum)

print(maximum_wealth)

