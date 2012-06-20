#!/usr/bin/env python

import os
import urllib

print """
OK! First, terms!

This page contains data files from the National Survey of Family Growth
(NSFG), for use with the book Think Stats by Allen B. Downey.

These data are also available from the CDC; the only difference is that
the files here are compressed with gzip. Note: if you have any problems
using the compressed versions, please contact the author, not the CDC.

Federal law provides that these data may be used only for the purpose of
health statistical reporting and analysis. Any effort to determine the
identity of any person or establishment is prohibited.

By downloading these data, you signify your agreement to comply with the
following legal requirements:

    To use these data for statistical reporting and analysis only;

    To make no use of the identity of any person or establishment discovered
    inadvertently and advise the Director, NCHS, of any such discovery; and

    To not link this data set with individually identifiable data from any
    other data set.

    In addition to those legal requirements, I would like to add the
    following ethical reminder:

    These files contain data collected from people who were asked to provide
    personal information for statistical purposes. Some of this information
    may be considered sensitive. Statisticians should work with this or any
    other statistical data with appropriate respect for the people who
    answered the questions.

I accept these terms.
"""

while True:
    msg = raw_input('type yes and enter to accept: ')
    if msg.strip().lower() == 'yes':
        break

urls = [
    'http://greenteapress.com/thinkstats/2002FemPreg.dat.gz',
    'http://greenteapress.com/thinkstats/2002FemResp.dat.gz',
    'http://thinkstats.com/survey.py'
    ]

program_dir = os.path.dirname(__file__)
for url in urls:
    fname = os.path.basename(url)
    with open(os.path.join(program_dir, fname), 'w') as f:
        print 'downloading %s...' % url
        data = urllib.urlopen(url).read()
        f.write(data)

print
survey_path = os.path.join(program_dir, 'survey.py')
execfile(survey_path)

print
print 'Now you should probably look at survey.py. Here it is...'
os.system('open -R %s' % survey_path)