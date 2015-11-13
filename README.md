#git-history-data

git-history-data analyses a Git source code repository and dumps out data in a form that is easy to analyse. In its simplest form it prints out one line for every change to every file in history, and who made the change, like this:

    $ cd myrepo
    $ git-history-data
    "Commit",  "Date",       "Author", "Added", "Removed", "File"
    "e35a4f0", "2015-11-11", "Pete",   1,       1,         "githistorydata/main.py"
    "5a6172d", "2015-07-15", "Andy",   1,       0,         "githistorydata/codeline.py"
    "5a6172d", "2015-07-15", "Andy",   8,       2,         "githistorydata/commitdetail.py"
    "5a6172d", "2015-07-15", "Andy",   32,      0,         "githistorydata/dataline.py"
    "5a6172d", "2015-07-15", "Andy",   8,       13,        "tests/git_parsing__test.py"
    "12f2881", "2015-07-13", "Pete",   4,       4,         "githistorydata/git.py"
    "8fd2224", "2015-07-13", "Andy",   18,      0,         "githistorydata/commitdetail.py"


It is intended to be easy to analyse the results in a tool such as [Watson Analytics](http://watsonanalytics.com), and to be convenient to manipulate with standard Unix command-line tools.

For example, if you want to see very large changes to a specific file (in the Git project itself):

    $ cd git
    $ git-history-data > git-git-history.csv
    $ grep "diff.c" git-git-history.csv | awk -F',' '{print $4, $3, $1 }' | sort -n -r | head -5
     4047  "Junio C Hamano" "3686aa1caf907d22fe318c28efe93f0e7870ba50"
     1805  "Martin Langhoff" "e660e3997fbad830e5723336d61883f3a50dbc92"
     1803  "Junio C Hamano" "c66b6c067e49c5ec80f1254daef79aa1c7f5ffce"
     1795  "Junio C Hamano" "e9b5b75ca87f45292de8ecde5d4d0512ac9542cd"
     1795  "Junio C Hamano" "b8ed7f0f40743dae6111c8950ba55051933298ca"

Or the files with terrifying numbers of authors:

    $ awk -F', ' '{print $6, $3}' git-git-history.csv | sort | uniq | awk '{arr[$1]++}END{for (a in arr) print arr[a], a}' | sort -n -r | head -5
    235 "Makefile"
    198 "Documentation/config.txt"
    137 "cache.h"
    130 "git-svn.perl"
    115 "diff.c"

##Prerequisites

git-history-data requires Git, Python 3 and the Python DateUtil library.  On Debian, Ubuntu and similar you can install these with:

    sudo apt-get install git python3 python3-dateutil

##Install

Get the code:

    TODO

Now add a line to your PATH by doing something like this:

    echo 'export PATH="$PATH:${HOME}/git-history-data"' >> ~/.bashrc

(Log out and back in again, and use `echo $PATH` to check your PATH has been updated.

##Use

`cd` into the working tree of a git repository, and then run `git-history-data`, redirecting the result to a file.  For example:

    cd git
    git-history-data > hist.csv

Now hist.csv contains one line per file per commit in the entire history of the project, showing the commit ID, timestamp, author and the number of lines added and removed in that file in that commit.

That's it.


