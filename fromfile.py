# Create a PDF given an item UUID for an item in NYPL's Digital Collections

import requests
import urllib
import os.path
import string
import sys
import subprocess

fname = raw_input('Enter the name of the file that has the captures (one capture per line): ')


#Setting the derivative type -- these are the possible deriv type values:
    # b - Center cropped thumbnail .jpeg (100x100 pixels)
    # f - Cropped .jpeg (140 pixels tall with variable width)
    # t - Cropped .gif (150 pixels on the long side)
    # r - Cropped .jpeg (300 pixels on the long side)
    # w - Cropped .jpeg (760 pixels on the long side)
    # q - Cropped .jpeg (1600 pixels on the long side) N.B. Exists only for public domain assets
    # v - Cropped .jpeg (2560 pixels on the long side) N.B. Exists only for public domain assets
    # g - a "full-size" .jpeg derivative N.B. Exists only for public domain assets
print 'For basic PDFs, best choice of derivative is going to be Q'
deriv_type = raw_input('Enter a derivative type: ')

captures = [line.rstrip('\n') for line in open(fname)]

print captures

img_url_base = "http://images.nypl.org/index.josh.php?id="

j = 1

for i in captures:

	if not os.path.isfile(str("%04d" % j)+'_'+str(i)+str(deriv_type)+'.tif'):
		urllib.urlretrieve(img_url_base+str(i)+'&t='+str(deriv_type)+'&download=1', str("%04d" % j)+'_'+str(i)+str(deriv_type)+'.tif')
		print "%s done, %s of %s" % (int(i), j, len(captures))
		j +=1
	else:
		print "file %s as %s deriv type already exists" % (i, deriv_type)
		j +=1