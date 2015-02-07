#!/usr/bin/env python

import urllib2
import sys

TARGET = 'http://crypto-class.appspot.com/po?er='
ct = ['58b1ffb4210a580f748b4ac714c001bd',
      '4a61044426fb515dad3f21f18aa577c0',
      'bdf302936266926ff37dbf7035d5eeb4']
iv = 'f20bdba6ff29eed7b046d1df9fb70000'

#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:
            print "We got: %d" % e.code       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding

    def guess(self, pos, guessed):
        pad = "%02x" % (pos + 1)
        for i in range(0, pos):
            pad += "%02x" % (pos + 1)

        for g in range(0, 256):
            guess = "%02x" % g
            guess += guessed
            guess_block = "%032x" % (int(ct[1], 16) ^ int(guess, 16) ^ int(pad, 16))
            q = iv + ct[0] + guess_block + ct[2]
            if self.query(q):
                return guess

if __name__ == "__main__":
    po = PaddingOracle()

    answer = '090909090909090909'
    for i in range (9, 16):
        answer = po.guess(i, answer)
        print answer
        print answer.decode("hex")
