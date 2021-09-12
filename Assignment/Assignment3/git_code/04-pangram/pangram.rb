# Q4
class Pangram
  def self.is_pangram?(str)
    ('a'..'z').all? { |word| str.downcase.include? (word) }
  end
end
