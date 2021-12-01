#!/usr/local/bin/perl -w
# usage: pre-processing.pl stop_words.txt replace.txt > new.txt
use English;

# open words.txt and stop_words.txt, store them in WORDS and REPLACE respectively
open(WORDS, shift @ARGV) or die "fail to open stop_words.txt: $!";
open(REPLACE, shift @ARGV) or die "fail to open replace.txt: $!";

my @words;  # array to store every word in stop_words.txt
# get all words into an array
while ($_=<WORDS>) { 
  chop; # strip eol
  push @words, split; # break up words on line
} 

# (optional)
# sort by length (makes sure smaller words don't trump bigger ones); ie, "then" vs "the"
@words=sort { length($b) <=> length($a) } @words;

# slurp text file into one variable.
undef $RS;
$text = <REPLACE>;

# now for each word, do a global search-and-replace; make sure only words are replaced; remove possible following space.
foreach $word (@words) { 
    $text =~ s/\b\Q$word\E\b\s?//sg;
}

# while ($_=$text) {
#     print $_ if s/^\s*//p;
# }

# output "fixed" text
print $text;