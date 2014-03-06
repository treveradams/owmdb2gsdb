Open WLAN Map Database to Grid-Square Database Converter Program (owmdb2gsdb)
============================================================================

This program is designed to allow one to convert the Open WLAN Map
Database to many more, much smaller Grid-Square Databases.

Both formats are the same CSV. One just is one huge file, while
the other is many smaller files.

KLUDGE ALERT!

Yes, this is a kludge. It may get better. It does the job.


BE A GOOD NETIZEN
=================
Please, be a good citizen. Do not download the database from the Open WLAN
Map project more than once a week. It is updated nightly, so doing it multiple
times a day would be counter productive. As it is hosted generously by an
individual, do not abuse the system. Go as long as you can between downloads.
Certainly do not download it more than any guidelines given on the project's
website. Thank you!


HOW TO USE IT
=============

Place this script and the db.csv file from the Open WLAN Map project
into the same directory. It should not contain any other files/data.

Run the script, without any arguments. It will create a gsdb directory
and place the appropriate data in the appropriate files within that
directory.

These files will be 3 levels of grid-square information. At my latitude,
these are just about 1 mile by .3 miles in size. This keeps the data small
and manageable for such uses as my "Open WLAN Map Public Data Visualizer."


Getting Support
===============
This is F/OSS. I will provide some support for this, but don't expect too much
for no money! If you want to help fix something or add a feature, I am very
interested in hearing from you.
