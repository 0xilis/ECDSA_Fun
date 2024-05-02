# ECDSA_Fun
Doing dumb fooling around with ECDSA-P256.

# ECDSA Signature Generation Formula

(Thanks to [this PS3 writeup from fail0verflow](https://fahrplan.events.ccc.de/congress/2010/Fahrplan/attachments/1780_27c3_console_hacking_2010.pdf) for helping me learn about how signatures are generated)

In every signature, you have r,s. e is the SHA256 hash of the data that is being verified. m is a secret random 256bit number. k is the 256bit private key.

The formula is S = (e + kR) / m. We already have e, S, and R, but what prevents us from solving for k is we don't know m.

If a random number generator is perfect, than m has a 25% chance of being within (1,256_BIT_MAX/4). This is only in scenarios where m has relation to nothing and is just a random 256bit number, and isn't accounting for possible minimum bit length.

### The fun

[GetMaxOfPrivateKeyWithMMax.py](https://github.com/0xilis/ECDSA_Fun/blob/main/GetMaxOfPrivateKeyWithMMax.py) contains code for getting a number that you know the private key cannot be greater than from a cert. Ex, in cenarios where m has relation to nothing and is just a random 256bit number, and isn't accounting for possible minimum bit length, m has a 25% chance of having a max of 256_BIT_MAX/4. This means you could plug in 256_BIT_MAX/4 and there *should* be a 25% chance that it will give you a number k cannot be larger than. This isn't a complete reveal of k since we don't know m specifically, but it can shorten our range of possible k values.
