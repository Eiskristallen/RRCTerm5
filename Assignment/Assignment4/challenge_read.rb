require_relative 'ar.rb'

# number_of_products = Product.count
# puts "There are #{number_of_products} in the products table."

# #Q1
# products_startwith_C_price_higher_than_ten = Product.where('name LIKE "c%"').where('price>10')
# for product in products_startwith_C_price_higher_than_ten do
#   puts product.name
# end
# #Q2
# products_with_low_quantity = Product.where('stock_quantity<5.0')
# for product in products_with_low_quantity do
#   puts product.name
# end

# Association1
category = Product.where(:name => "Chai").first
puts category.category.id
# Association2
# category2 = Category.where(:name => "Beverages").first
# new_one = category2 .products.build( 
#   name:  "NewProduct5",
#   description: "NewProduct5 description",
#   price:  9.5,
#   stock_quantity:  65
# )
# Association3
Category.where(:name => "Beverages").first.products.where('price<5.0').each do |product|
  puts product.name
end
