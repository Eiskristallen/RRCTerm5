#Qingbei Huang Q1
class HelloWorld
  def self.hello(input="Hello, World!")
    if input !="Hello, World!"
      puts "Hello, #{input}!"
      return "Hello, #{input}!"
    else
      puts "Hello, World!"
      return "Hello, World!"
    end
  end
end

HelloWorld.hello

