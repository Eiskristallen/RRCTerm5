require_relative 'ar.rb'

categories = Category.all();
puts categories
categories.each do |category|
  puts "category name: #{category.name}"
  category.products.each do |product|
    puts "  product name: #{product.name}
            product price: #{product.price}"
  end
end