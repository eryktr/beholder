[![codecov](https://codecov.io/gh/eryktr/beholder/branch/master/graph/badge.svg?token=A0N7L9YHXS)](https://codecov.io/gh/eryktr/beholder)

# beholder
A tool to inform about latest updates on websites it tracks

# Usage
    usage: beholder [-h] [-t TIME] [-o OUTPUT_PATH] [-d] config_path

    positional arguments:
      config_path           Path to the config file containing website addresses.

    optional arguments:
      -h, --help            show this help message and exit
      -t TIME, --time TIME  Number of seconds between subsequent checks. (default: 5)
      -o OUTPUT_PATH, --output_path OUTPUT_PATH
                            File where the session should be dumped. (default: None)
      -d, --show_diffs      Display not only if something changes but also what changes. (default: False)

# Config path
Config path should be your file with its location. The content inside file should look like this:
    
    protocol://your_first_website
    protocol://your_second_website
    protocol://your_third_website
    ...
    protocol://your_nth_website

In other words, file should contain valid website URLs, each of them separated by a newline, where:
* protocol - is either http or https
* your_nth_website - is a valid website
 
 # Examples of usage
Content of file.txt:
 
    http://www.mediamond.fi/
    https://eryktr.github.io/
    
Standard session:
 
    beholder file.txt
    
    2020-04-26 23:40:19.002276 - http://www.mediamond.fi/ - Website has changed.
    2020-04-26 23:43:23.244814 - http://www.mediamond.fi/ - Website has changed.

Session with diffs:
 
    beholder -d file.txt
    
    2020-04-26 23:50:26.718035 - http://www.mediamond.fi/ - Website has changed.
    ---

    +++

    @@ -195,7 +195,7 @@


     DSJ4 Online

    -       Currently playing: 4
    +       Currently playing: 3


     DSJ3 Online
     
     2020-04-26 23:55:14.683506 - http://www.mediamond.fi/ - Website has changed.
     ---

     +++

     @@ -195,7 +195,7 @@


     DSJ4 Online

     -       Currently playing: 3
     +       Currently playing: 4


     DSJ3 Online



# Python requirement
Beholder requires Python >= 3.8.0.

# Installation (for developers)

    sudo apt install python3.8-venv
    python3.8 -m venv env
    source env/bin/activate
    pip3 install -e .[dev]
