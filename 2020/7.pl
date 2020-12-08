#!c:\bin\perl\bin\perl.exe -w

$filename = "7ex1.txt";

%listofbags = getlinesfromfile($filename);

# ~ while (($key, $vals) = each(%listofbags))
# ~ {
	# ~ print "key=$key, value(s)=$vals\n";
# ~ }

print numberofbaginside("dark olive")-1; # should be 7
print numberofbaginside("shiny gold")-1; # inside shouldn't count this one bag

sub numberofbaginside(){
  $bag = shift;
  my $ans = 0;
  print("\n\nlooking for bags in $bag;;;");
  if ($listofbags{$bag}) {
    my $value = $listofbags{$bag};
    my @vals = split(/ *, */,$value);
    foreach (@vals){
      print("one of the $bag vals is $_\n");
      if (/^\d/) {
        print ("hey23\n");
        ($qty,$bagn) = ($_ =~ /^(\d+) (.*)$/);
        print ("hey25 q=$qty, newbag=$bagn, _=$_\n");
        $ans += 1 + $qty * numberofbaginside($bagn);
        return  $ans;
      } else {
        print("hey 28\n");
        return 1; # the bag itself
      }
    }
  } else {
    print ("hey 33\n");
    return 0;
  }
  return $ans;
}

sub getlinesfromfile(){
  my $filename = shift;
  my %ans;
  open($FN,$filename) or die "Can't open file $filename";
  while (<$FN>) {
      my ($key,$value) = split / bags contain /;
      $value =~ s/ *bags*\.*//g;
      # print("key=$key values=;;;" . join(";;;",@vals));
      $ans{$key} = $value;
  }
  return %ans
}
