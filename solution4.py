# Given:
#     1. A list of "user identities" containing the ID number and name of 9 users
#     2. A list of "connection pairs' containing all unique connections between users
# Find:
#     The number and identities of each user's connections
__author__ = 'Onyedikachi Udeh'

users = [{'id': 0, 'name': 'Hero'}, 
        {'id': 1, 'name': 'Dunn'}, 
        {'id': 2, 'name':'Sue'}, 
        {'id': 3, 'name': 'Chi'}, 
        {'id': 4, 'name': 'Thor'}, 
        {'id': 5, 'name': 'Clive'}, 
        {'id': 6, 'name': 'Hicks'}, 
        {'id': 7, 'name': 'Devin'}, 
        {'id': 8, 'name': 'Kate'}, 
        {'id': 9, 'name': 'Klein'}]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for each_user in users:
    number_of_conns = 0
    connection_names = []
    for i in friendships:
        if each_user['id'] in i:
            number_of_conns += 1
            if i.index(each_user['id']) == 0:
                position = i[1]
                connection_names.append(users[position]['name'])
            elif i.index(each_user['id']) == 1:
                position = i[0]
                connection_names.append(users[position]['name'])

    print(f"{each_user['name']} has {number_of_conns} connection(s)")
    print(f"Identities of the connection(s) : {connection_names} \n")


###############################################################
# OUTPUT
###############################################################
# Hero has 2 connection(s)
# Identities of the connection(s) : ['Dunn', 'Sue'] 

# Dunn has 3 connection(s)
# Identities of the connection(s) : ['Hero', 'Sue', 'Chi'] 

# Sue has 3 connection(s)
# Identities of the connection(s) : ['Hero', 'Dunn', 'Chi'] 

# Chi has 3 connection(s)
# Identities of the connection(s) : ['Dunn', 'Sue', 'Thor'] 

# Thor has 2 connection(s)
# Identities of the connection(s) : ['Chi', 'Clive'] 

# Clive has 3 connection(s)
# Identities of the connection(s) : ['Thor', 'Hicks', 'Devin'] 

# Hicks has 2 connection(s)
# Identities of the connection(s) : ['Clive', 'Kate'] 

# Devin has 2 connection(s)
# Identities of the connection(s) : ['Clive', 'Kate'] 

# Kate has 3 connection(s)
# Identities of the connection(s) : ['Hicks', 'Devin', 'Klein'] 

# Klein has 1 connection(s)
# Identities of the connection(s) : ['Kate'] 