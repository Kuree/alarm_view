


out = []

digits =[ "0000001",
          "1001111", #1
          "0010010", 
          "0000110", #3
          "1001100",
          "0100100", #5
          "1100000",
          "0001111", #7
          "0000000", 
          "0001100", #9
         ]

for i in range(10000):
    s = "{:04d}".format(i)    
    out += ["{:21d} 0 0 {} {} {} {}".format(i,
                                           digits[int(s[0])],
                                           digits[int(s[1])],
                                           digits[int(s[2])],
                                           digits[int(s[3])] 
                                           ) ]
f = open ("examples/count.out", "w")
f.write("\n".join(out))
f.close()