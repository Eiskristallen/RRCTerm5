require_relative 'ar.rb'

new_product_one = Product.where(:name => 'NewProduct1').first
new_product_one.destroy  unless new_product_one.nil?