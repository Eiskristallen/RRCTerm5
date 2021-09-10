# Q2 
class HelloWorld
  attr_accessor :name
  def initialize(name)
    @name = name
  end
  def hello(input="Hello, World!")
    if input !="Hello, World!"
      puts "Hello, #{input}. My name is #{name}!"
      return "Hello, #{input}. My name is #{name}!"
    else
      puts "Hello, World. My name is #{name}!"
      return "Hello, World. My name is #{name}!"
    end
  end
end