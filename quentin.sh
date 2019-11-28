#!/usr/bin/env perl

    use 5.010;
    use strict;
    use warnings;
     
	for (my $i = 0; $i <= 99 ; $i++) {
		my $string = "is";
		open(FILE, "<test4.txt") or die "Could not open file: $!";
		my ($lines, $totalwords, $words) = (0,0,0);
		while (<FILE>) {
			$lines++;
			$totalwords += scalar(split(/\s+/, $_));
			if (/$string/)
			{
				$words++;
			}
		}
		print("lines=$lines words=$totalwords nombre total de $string = $words\n");
		close(FILE); 
    }
