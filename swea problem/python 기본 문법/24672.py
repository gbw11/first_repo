mail = input()
idx = mail.find("@")


if idx == -1: print("Invalid email")
else: print(mail[idx+1:])
'''
if idx == -1 or idx_2 == -1:
    print("Invalid email")
else:
    print(mail[idx+1:])
    '''