# Snoolie K, (c) 2024. Someone probably discovered this before me, but I wrote the code here.

# ECDSA Signature will have r,s. Input s here:

s = 99968551279127486218265796508415968333456545922193080466408016214828169622459

# Input the MAX value you know M can be.

# (Note: The base signature I have actually has an m larger than this but this is just for demo)
max_m = 28948022309329048855892746252171976963317496166410141009864396001978282409983

# Input r of signature here:

r = 46835780868727964423378794110917455833422857227467599002867243320095474356209

# Input e (sha256 hash of data) here:

e = 62468104609141918917072698772668338282552606356753848825115203154311296438194

# ECDSA signatures are S = (e + kR) / m
# Which we can also represent as Sm = (e + kR)

# So, we can substiture the m for max_m+1

biggerThanSm = s * (max_m+1)
print("e+kR can't be greater than: " + str(biggerThanSm))

# Then we know the value of e + kR can't be larger than S*(max_m+1)

# Now we just subtract e from e + kR so we have a value we know kR can't be larger than

biggerThanKR = biggerThanSm - e
print("kR can't be greater than: " + str(biggerThanKR))

# Then we divide R from kR to have a value we know k can't be larger than

biggerThanPrivateKey = (biggerThanKR / r)

print("Assuming m is in the range [1, " + str(max_m) + "]: ")
print("Private key MUST be smaller than: " + str(biggerThanPrivateKey))
print("I, Snoolie K discovered this myself, but to be honest someone definitely has discovered this before me and I just didn't know... please tell me who if you know so I can credit them!")
