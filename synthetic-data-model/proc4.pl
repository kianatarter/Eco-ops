#!/usr/bin/perl

use strict;
use warnings;
use JSON; # Make sure to have the JSON module installed

# Path to the input JSON file and output (corrected) JSON file
my $input_file = 'ot6_data.json';
my $output_file = 'ot7b.json';

# Read the entire file content
open(my $fh, '<:encoding(UTF-8)', $input_file)
  or die "Could not open file '$input_file' $!";

my $file_content = do { local $/; <$fh> };
close($fh);

# Replace incorrectly quoted keys and values
$file_content =~ s/'\s*([^']+?)\s*'\s*:/\"$1\":/g; # Fix keys
$file_content =~ s/:\s*'([^']+?)'\s*(,|\})/:\"$1\"$2/g; # Fix string values

# Attempt to parse and pretty-print the JSON to ensure its validity
my $json = JSON->new;
my $data;
eval {
    $data = $json->decode($file_content);
};
if ($@) {
    die "Error parsing JSON text: $@";
}

# Save the corrected and pretty-printed JSON back to a file
open(my $fh_out, '>:encoding(UTF-8)', $output_file)
  or die "Could not open file '$output_file' $!";
print $fh_out $json->pretty->encode($data);
close($fh_out);

print "JSON file has been processed and corrected.\n";

