puts "with each loop"
(1..10).to_a.each do |i|
    puts "value #{i}"
end

puts "each with index"
(1..10).to_a.each_with_index do |i, index|
    puts "value #{i} and index is #{index}"
end

puts "select"
arr = (1..10).to_a.select do |i|
    i % 2 == 0
end

puts arr

puts "reject"
arr = (1..10).to_a.reject do |i|
    i % 2 == 0
end

puts arr

puts "upto"
1.upto(5) do |i|
    puts i
end

puts "downto"
5.downto(1) do |i|
    puts i
end

puts "collect"
arr = (1..10).to_a.collect do |i|
    i*2
end

puts arr

puts "each"
arr = []
(1..10).to_a.each do |i|
    arr.push(i*2)
end

puts "Each value #{arr}"

puts "map"
arr = (1..10).to_a.map do |i|
    i*2
end

puts arr

puts "Addition og=f 1 to 10 is #{(1..10).inject(:+)}"

(1..10).to_a.inject(0) do |sum, i|
    sum += i
end