arr = (1..100).to_a.select do |i|
    i % 3 == 0 and i % 5 == 0 
end

puts "#{arr}"