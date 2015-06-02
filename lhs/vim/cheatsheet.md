Cheatsheet
==========

Basic Commands
--------------

+ Changing Modes
    - i           Insert mode at cursor
    - a           Insert mode after cursor
    - I           Insert mode at beginning of line
    - A           Insert mode at end of line
    - `<Esc>`     Leave insert mode (return to normal mode)

+ Movement (only in 'Normal' mode)
    - h           Move left
    - j           Move down
    - k           Move up
    - l           Move right
    - `<Ctrl>`b   Move back a page
    - `<Ctrl>`f   Move forward a page

+ Saving, Quitting ('Normal' mode)
    - :w          Write the file to disc (save)
    - :q          Close the current file
    - :wq         Write the file to disc and close it
    - :q!         Force quit without saving changes
    - ZZ          Saves and quits

Searching Files
---------------

+ Basic Search
    - /bunnies       Look for the string 'bunnies' withing the document
    - n              Find the next occurance of the last searched string
    - N              Find the previous occurance of the last searched string

+ Search and Replace
    - :s/foo/bar      Replace first instance of 'foo' on current line with 'bar'
    - :s/foo/bar/g    Replace every instance of 'foo' on current line with 'bar'
    - :s/foo/bar/gc   Replace every instance of 'foo' on current line with 'bar'
                        but ask for confirmation first
    - :%s/foo/bar/g   Replace every instance of 'foo' in the file with 'bar'
    - :%s/foo/bar/gc  Replace every instance of 'foo' in the file with 'bar' but
                        ask for confirmation first
