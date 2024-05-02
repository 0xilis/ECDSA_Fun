# Snoolie K, (c) 2024. Someone probably discovered this before me, but I wrote the code here.

# The maximum 256bit integer 
max = 115792089237316195423570985008687907853269984665640564039457584007913129639935

# ECDSA Signature will have r,s. Input s here:

s = 99968551279127486218265796508415968333456545922193080466408016214828169622459

# Input r of signature here:

r = 46835780868727964423378794110917455833422857227467599002867243320095474356209

# Input e (sha256 hash of data) here:

e = 62468104609141918917072698772668338282552606356753848825115203154311296438194

m_times_s_mx = (max * r) + e

max_m = m_times_s_mx / s

if max_m > max:
  # We can't get max_m, but we can get max_k
  max_k = ((max * s) - e) / R
  print("k MUST be smaller than: " + str(max_k))
else:
  print("m MUST be smaller than: " + str(max_m))

print("I, Snoolie K discovered this myself, but to be honest someone definitely has discovered this before me and I just didn't know... please tell me who if you know so I can credit them!")
