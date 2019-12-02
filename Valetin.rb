ligne=0
word=0
counter=0
for i in (1..10000)	
	File.open("UTF.txt").each do |line|

		ligne=ligne+1
		array = line.strip.split(" ")
		word += array.size

		array.each do |ct|
			if (ct.include? "is")
				then counter+=1
			end
		end	
	end 
end 
puts "ligne:  #{ligne}" 
puts "word: #{word}"
puts "is: #{counter}"	
