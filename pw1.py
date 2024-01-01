import sys, pyperclip

PASSWORDS = {'sreten':'spass', 'petar':'ppass', 'irisa': 'ipass', 'toda':'tpass'}

if len(sys.argv) < 2:
    print('Usage: python pw1.py account_name')
    sys.exit()
    
account = sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f"Password for {account} has been copied to clipboard.\n")
else:
    print(f"Password for {account} does not exist.")


