require_relative 'ar.rb'

products = Product.where('stock_quantity<40.0')

products.each do |product|
  product.stock_quantity = (product.stock_quantity + 1)
  product.save
end