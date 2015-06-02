Vim Excercise 1
===============

Vim is a powerful text editor. This guide will demonstrate some of the features
of vim. Best served in vim.

Read through the bullets first, then do the activities in the boxes with as few
keystrokes as possible.

There are many great tutorials for Vim online:

-   [Interactive Vim Tutorial - Open Vim](http://www.openvim.com/tutorial.html)
-   [Vim Wiki Tutorial](http://vim.wikia.com/wiki/Tutorial)
-   [Vim Golf](http://www.vimgolf.com/)


Movement
--------

-   `h,j,k,l` move around this document
-   `w` moves forward a word, `b` moves back
-   `Ctrl-f` and `Ctrl-b` move forward and back pages

```
Get to the 'h' in 'here' using the navigation keys.
Jump to the end of this word using `w`, go back to 'keys' above using `b`.


Then jump straight to this line using `3j`.
And finally jump forward and back using `Ctrl-f` and `Ctrl-b`.
```


Inserting text
--------------

-   Press `i` to insert text at the cursor (enter insert mode)
-   Press `I` at the beginning of a line, `A` at the end
-   Press `Esc` to leave insert mode

```
Navigate to the       and place the word 'blank' there.
Using `A`, place the word that describes it's position at the
the text 'Place' at the beginning of the line using `I`.
```


Copying and pasting
-------------------

-   Ensure that you are in 'Normal' mode by pressing `Esc`
-   Yank (copy) a line of text using `yy`
-   Paste the line of text using `p`
-   Delete (cut) a line of text using `dd`
-   Cut a character using `x`

```
Copy this line of text using `yy`.
Then navigate to this line, and paste it using `p`.
Then cut this line using `dd`, and place it at the top of this block.

Then cut all four of 'these' lines by calling `4dd` on this line.
This is a 'these' line.
This is a 'these' line.
This is a 'these' line.

Cut an 'o' from 'good' using `x` and paste it in 'hell'.
```

-   Delete the rest of a line (from cursor on) using `Shift-d`
-   Delete three words using `d3w` or `3dw`

```
Delete everything after here on this line.
Delete these four words from this line.
```


Undoing mistakes
----------------

-   `u` to undoes your last command
-   `Ctrl-R` redoes your command

```
Delete this line with `dd` and bring it back with `u`.
Then paste it after this line with `p`, and remove it again with `u`.
Delete this line with `dd` and bring it back with `u`.
Re-delete it with `Ctrl-R`.
```

Protip: Abuse `u` and `Ctrl-R`, they remember quite a bit for you.


Copying and pasting multiple lines
----------------------------------

-   Ensure you are in 'Normal' mode, then enter 'Visual' mode by pressing `v`.
-   Use normal navigation to select the text you want to copy/cut
-   `x` to cut the selected text
-   `p` to paste the selected text
-   Use the `.` operation to replay the last command.

```
cut both this line
and this line

to move them after this line

paste those two lines again after this line by pressing `.` on the next line
```


Searching for strings
---------------------

-   From normal mode, press `/` to begin a search
-   Type your search term, then press `Enter`
-   Press `n` to scroll through the matches forward, `N` for backward

```
Find me first, find me third,
and find me second.
```

-   Use searching for easy, quick, and accurate navigation. Especially useful when
    looking for function definitions with really specific names.

```
Jump to the bottom line by searching for a word in it, then delete it with `dd`.

And, as in uffish thought he stood,
  The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
  And burbled as it came!
```


String substitution
-------------------

-   From normal mode, go into command mode by pressing `:`
-   Command: `s/s/r` to replace 's' with 'r'
-   Command: `%s/s/r` to do it for every line in the file
-   Command: `s/s/r/g` to do it globally for this line
-   Command: `s/s/r/gc` to do it globally for this line and ask for confirmation

```
Replace this 'foo' but not this 'foo' with 'bar' using `:s/foo/bar` on this line
Replace both this 'foo' and this 'foo' with 'bar' using `:s/foo/bar/g`
Replace this 'foo', not this 'foo', and this 'foo' using `:s/foo/bar/gc`
Replace this 'foo', but not this 'foo', using the `.` command on this line.
```

-   Combine with the 'visual' mode to apply to a whole region of text
-   Undo your action with `u`

```
Select the block below using `v`, then in visual mode use `:s/foo/bar/g`
This 'foo' should not turn into a 'bar'.

Select the foo's in this paragraph starting here and pressing `v`
Navigate to the end of the foo-paragraph
On the last foo-line use the command `:s/foo/bar/g` to make it a bar-paragraph
```


Reading in data from another file or command
--------------------------------------------

-   Use `:! <command>` to run `command` in your shell
-   Use `:read <filename>` to read text from another file into this file
-   Use `:read ! <command>` to read the result of `command` into this file

```
Check what files are in the current directory with ':! ls'
Read the contents of 'jabberwocky' into the space between the '##'s
    ##

    ##

Read in a sequence of numbers from 0 to 15 by 2's using `:read ! seq 0 2 15`
    ##

    ##
```
