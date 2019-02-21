# sum of the squares of first 10 natural numbers
sum1 = 0
sum2 = 0
(1..100).to_a.each do |i|
    sum1 += i**2
    sum2 += i
end
# sum2 = sum2**2
# puts sum1
# puts sum2

# difference = sum2 - sum1

puts "defference is #{sum2*sum2 - sum1}"

ans = (((1..10).inject(:+))**2) - ((1..10).collect{|i| i*i}.inject(:+))
puts "One line #{ans}"