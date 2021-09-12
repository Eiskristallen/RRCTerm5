# Q5
class Grains
  def self.square(grains)
   return 2 ** (grains - 1)
  end
  def self.total()
    total_num = 0
    for value in 1..64 do
      total_num += square(value)
    end
    return total_num
  end
end
puts Grains.total