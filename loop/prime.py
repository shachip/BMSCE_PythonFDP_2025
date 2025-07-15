n=60
i=2
is_prime = True
if n<2:
    is_prime=False
else:
    while i<n:
        if n%i==0:
            is_prime=False
            break
        i += 1
print("Prime" if is_prime else "Not Prime")