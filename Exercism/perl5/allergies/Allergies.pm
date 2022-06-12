package Allergies;
use strict;
use warnings;
use Exporter qw<import>;
our @EXPORT_OK = qw<allergic_to list_allergies>;

my %allergies = (
  1   => "eggs",
  2   => "peanuts",
  4   => "shellfish",
  8   => "strawberries",
  16  => "tomatoes",
  32  => "chocolate",
  64  => "pollen",
  128 => "cat"
);

# Nearest power of 2, less than or equal to $num.
sub nearest_power_of2 {
  my ($num) = @_;
  my $count = 0;

  while ($num) {
    $count++;

    last if ( $count == 8 );    #  Break. (At 8? Since we will subtract 1 later)

    $num = $num >> 1;
  }
  return 2**( $count - 1 );
}

sub list_allergies {
  my ($score) = @_;
  my $list = [];
  while ($score) {
    my $nearest_power_of2 = nearest_power_of2($score);
    push( @{$list}, $allergies{$nearest_power_of2} );
    $score = $score - $nearest_power_of2;
  }
  return $list;
}

sub allergic_to {
  my ($input) = @_;

  return 0 if $input->{'score'} == 0;

  my $nearest_power_of2 = nearest_power_of2( $input->{'score'} );

  return int( $nearest_power_of2 / nearest_power_of2() ) == 0;
}

1;
