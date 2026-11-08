# Python3 Worklog Project

Terminal application for logging what work someone did on a certain day. Application stores information in a CSV file
and allows for search by date or a plain text search. Also can generate reports.

## Goals

* Program provides a menu with options to add entry, search entries, or quit
* When adding an entry user can give task a title, time spent (in minutes), notes
* User can delete and edit existing records changing title, time spent, and notes
* Entries are saved to a new row in a CSV file with columns for date, task, name, time spent, and notes
* Users can search by date, time spent, exact search, regex pattern, and date ranges
* Entries are displayed one at a time with the ability to page forward and backward
* Complies with most common PEP 8 standards

## Architecture map

Download and open the [offline Floorplan](docs/floorplan/index.html), or read the [map guide](docs/floorplan/README.md). The map follows actual source processing and documents unfinished features; it is not application runtime verification.
