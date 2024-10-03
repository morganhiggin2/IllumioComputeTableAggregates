## Assumptions

* This was ran and tested using the Python 3.10.12 version.
* The accuracy of the results in the output file were compared to the by-hand calculations of the sample data provided in the assignment.
* The sample data is provided, the sample data is stored in two files in ASCII format,
  - Flow logs: data/flow_logs.txt
  - Lookup table: data/lookup_table.csv
* The requirement 'The matches should be case insensitive' applies to the tag matching. Because this is case insensitive, all tags have been converted to their lower counterpart. This is because if there are two tags that are the same regardless of their case sensitivity, we have to choose which tag variation to keep, as case does not matter. We are going to default to the lower form of the tag.
* This file only supports the default log format, and the only version it supports is version 2.
* The results of the content will be outputted to a file named 'output.txt' in the same base directory of the main.py file.
* The results for each aggregate are not in any particular order.
* Each aggregate in the 'output.txt' file is displayed in the following format:
  - Title
  - Header
  - Rows in header order...
* This program completed in O(len(F) + len(L)) time, where F is flow logs, L is the lookup table, and len returns the number of rows of that table.
* The space complexity is O(size(F) + size(L)) space, where size() returns the size of the table.

Author: Morgan Higginbotham
