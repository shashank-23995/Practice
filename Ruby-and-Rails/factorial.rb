puts "Enter n"
n = gets.chomp.to_i

factorial = 1
(1..n).to_a.each do |i|
    factorial = factorial * i
end

puts factorial