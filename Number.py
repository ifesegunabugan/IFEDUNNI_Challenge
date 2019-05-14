import re

for _ in range(int(input())):
    p = input().strip()
    try:
        # runs string against regex filters
        assert re.match(r'(\d{4}-){3}\d{4}$', p) or \
               re.match(r'\d{16}$', p)
        # finds any dashes and removes it
        n = re.sub(r'-', '', p)
        # makes sure sequence starts with 4, 5, or 6
        assert re.match(r'[456]', p)
        #ensures that there are no instances of a number appearing 4 times consecutively
        assert not re.search(r'(\d)\1{3,}', p)
        # any exceptions to the regex filters will print invalid
    except:
        print('Invalid')
    else:
        print('Valid')