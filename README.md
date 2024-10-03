## Assumptions

* The requirement 'The matches should be case insensitive' applies to the tag matching, because this is case insensitive, all tags have been converted to their lower counterpart. This is becuase, when if there are two tags which are the same irregardless of their case senstitvity, we have to choose which tag variation to keep, as case does not matter. We are going to default to the lower form of the tag.
* This file only supports the default log format, and the only version it supports is version 2
* The results of the content will be outputted to a file named 'output.txt' in the same base directory of the main.py file.
* The results for each aggregate are not in any particular order.
* Each aggregate in the 'output.txt' file is displayed in the following format
  Title
  Header
  Rows in header order...
* This program completed in O(len(F) + len(L)) time, where F flow logs, L is the lookup table, and len returns the number of rows of that table
* The space complexity is O(size(F) + size(L)) space, where size() returns the size of the table
