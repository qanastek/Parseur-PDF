line = 0
word = 0
is = 0

for i in (1..10000)

	File.open('fichierTest.txt').each do |current|

		line += 1

		word += current.strip.split(" ").size

		is += current.scan(/is/).length

	end

end

puts "Lignes: #{line}"
puts "Word: #{word}"
puts "Is: #{is}"