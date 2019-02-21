a = 5
puts "value of age is #{a}" # ruby interpolation
puts 'value of age is #{a}'

str = 'ruby'
puts "value of str is #{str}"

array = [1, 2.0, 'Rails']
puts "value of array is #{array}"

is_admin = true
puts "value of is_admin is #{is_admin}"

hash = {:language=>"Ruby", "framework"=>"Rails"}
puts "hash values #{hash}"
puts "hash keys #{hash.keys}"
puts "hash values #{hash.values}"
puts "language #{hash[:language]}"
puts "framework is #{hash["framework"]}"

range = (1..10)
puts "Range value is #{range.to_a}"