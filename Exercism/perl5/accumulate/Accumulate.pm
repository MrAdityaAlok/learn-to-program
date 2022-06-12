package Accumulate;
use strict;
use warnings;
use Exporter qw<import>;
our @EXPORT_OK = qw<accumulate>;

sub accumulate {
  my ( $list, $func ) = @_;
  my @result;
  foreach ( @{$list} ) {
    push @result, $func->($_);
  }
  return \@result;
}

1;
