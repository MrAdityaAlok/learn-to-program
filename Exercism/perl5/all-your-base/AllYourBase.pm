package AllYourBase;
use strict;
use warnings;
use Exporter qw<import>;
our @EXPORT_OK = qw<rebase>;

my @errors = (
  'input base must be >= 2',
  'output base must be >= 2',
  'all digits must satisfy 0 <= d < input base',
);

# Helper function to return hex representation of decimal.
sub to_hex {
  return ( 0 .. 9, "A" .. "F" )[ $_[0] ];
}

sub base10_to_baseX {
  my ( $num, $output_base ) = @_;

  return $num if ( $num == 0 );

  # Here num will be treated as string, since that's the context.
  return split( '', $num ) if ( $output_base == 10 );

  my @result;
  until ( $num == 0 ) {    # Until $num == 0, i.e until quotient is not 0, loop.
    my $converted = $num % $output_base;
    $num = int( $num / $output_base );    # int() to remove any fractional part.
    push( @result, $output_base == 16 ? to_hex($converted) : $converted );
  }

  return reverse @result;
}

sub rebase {
  my ( $digits, $input_base, $output_base ) =
    ( $_[0]->{'digits'}, $_[0]->{'inputBase'}, $_[0]->{'outputBase'} );

  if ( $input_base < 2 ) {
    die $errors[0];
  }
  elsif ( $output_base < 2 ) {
    die $errors[1];
  }

  my $base10_num = 0;    # Stores digits converted to base10.

  if ( $input_base == 10 ) {
    $base10_num = int( join( '', @{$digits} ) );    # Join digits together.
  }
  else {
    my $num_of_digits = scalar( @{$digits} );
    for ( my $i = 0 ; $i < $num_of_digits ; $i++ ) {
      die $errors[2] if !( -1 < $digits->[$i] < $input_base );
      $base10_num +=
        ( $input_base**$i ) * $digits->[ ( $num_of_digits - 1 ) - $i ];
    }
  }

  return [ base10_to_baseX( $base10_num, $output_base ) ];
}

1;
