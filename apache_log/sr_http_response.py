#!/usr/bin/python
### return Success rate from apache logs based on httpd code 200 
import sys
import re
import collections
def regexp(input):
        prog = re.compile('([0-9]*/[a-zA-Z]{3}/[0-9]{4}):([0-9]{2}:[0-9]{2}).* ([0-9]*) ([0-9]*)')
        result = prog.search(input)
        state = result.group(3)
        return state
def sr_calc(filename):
        f = open(filename,'rU')
        state_list= []
        for line in f:
                state_list.append(regexp(line))
        f.close()
        ct = collections.Counter(state_list)
        sum = 0
        for key in ct.keys() :
                sum = sum + ct[key]
        SR = ct['200']/float(sum)
        print 'SR = '+str(SR)
def main():
        sr_calc(sys.argv[1])

if __name__ == '__main__':
    main()
