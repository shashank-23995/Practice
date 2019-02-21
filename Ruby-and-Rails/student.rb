# no of students
# average percentage
# display_info method

class Student
    @@no_of_students = 0
    attr_accessor :name, :age, :marks

    def initialize(name)
        # @name = name
        @@no_of_students += 1
    end

    def user_input
        puts "Enter name"
        @name = gets.chomp
        puts "Enter age"
        @age = gets.chomp.to_i
        puts "Enter marks seperated by comma"
        @marks = gets.chomp.split(",").map{|num| num.to_i}
    end

    def average
        puts " average is #{@marks.sum/@marks.length}"
    end

    def percentage
        # puts "percentage is #{((@marks.sum)/((@marks.length)*100))*100}"
        # puts "percentage is #{((marks.inject(:+))/(marks.length*100)*100)}"
        puts "percentage is #{((@marks.sum)/((@marks.length)*100).to_f)*100}"
    end

    def display_info
        puts "Student info"
        puts "#{name} #{age}"

    end

    def self.get_no_of_students
        puts "Enter total number of students"
        @@no_of_students = gets.chomp
    end

end

s1 = Student.new('Shashank')
# Student.get_no_of_students
s1.user_input
s1.average
s1.percentage
s1.display_info