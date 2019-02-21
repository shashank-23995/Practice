arr = []
(11..99).to_a.each do |i|
    (11..99).to_a.each do |j|
        number = i * j
        str_number = number.to_s
        reverse_str = str_number.reverse
        if str_number == reverse_str
            arr.push(number) 
        end
    end
end

# print arr
puts "maximum number is #{arr.max}"