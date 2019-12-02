#!/usr/bin/env perl

    use 5.010;
    use strict;
    use warnings;
    
	my $titre = `head -1 test4.txt `;
	
	my $filename = 'report.txt';
	open(my $fh, '>', $filename) or die "Could not open file '$filename' $!";
	print $fh "titre:$titre";
	close $fh;

