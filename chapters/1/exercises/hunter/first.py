#!/usr/bin/python

import survey
table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)

# 2. Write a loop that iterates table and counts the number of live
#    births. Find the documentation of outcome and confirm that your
#    result is consistent with the summary in the documentation.
live_births = 0
for pregnancy in table.records:
    if pregnancy.outcome == 1:
        live_births += 1

print 'Live births: %d' % live_births

# 3. Modify the loop to partition the live birth records into two
#    groups, one for first babies and one for the others. Again, read
#    the documentation of birthord to see if your results are
#    consistent.
live_first_births = live_subsequent_births = 0
for pregnancy in table.records:
    if pregnancy.outcome == 1:
        if pregnancy.birthord == 1:
            live_first_births += 1
        else:
            live_subsequent_births += 1

print 'Live first births: %d' % live_first_births
print 'Live subsequent births: %d' % live_subsequent_births
assert live_births == live_first_births + live_subsequent_births

# 4. Compute the average pregnancy length (in weeks) for first babies
#    and others. Is there a difference between the groups? How big is
#    it?

first_pregnancy_lengths = [
    p.prglength for p in table.records if p.birthord == 1
    ]
mean_first_pregnancy_length = (
    sum(first_pregnancy_lengths) / float(len(first_pregnancy_lengths))
    )

subsequent_pregnancy_lengths = [
    p.prglength for p in table.records if p.outcome == 1 and p.birthord > 1
    ]
mean_subsequent_pregnancy_length = (
    sum(subsequent_pregnancy_lengths) / float(len(subsequent_pregnancy_lengths))
    )

assert len(first_pregnancy_lengths) + len(subsequent_pregnancy_lengths) == live_births
print 'Mean length of first pregnancy: %.1f' % mean_first_pregnancy_length
print 'Mean length of subsequent pregnancies: %.1f' % mean_subsequent_pregnancy_length