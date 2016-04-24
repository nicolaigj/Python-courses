daily_cost = 0.51 * 24
monthly_cost = daily_cost * 30
twenty_servers = daily_cost * 20
length_of_days = 918 / daily_cost
print('{0:15} | {1:8}$'.format('Daily',daily_cost))
print('{0:15} | {1:8}$'.format('Monthly', monthly_cost))
print('{0:15} | {1:8}$'.format('20 servers', twenty_servers))
print('{0:15} | {1:8} days'.format('Number of days', length_of_days))