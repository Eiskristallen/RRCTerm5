require_relative 'ar.rb'

# W1
new_product_one = Product.new
new_product_one.name  = "NewProduct1"
new_product_one.description = "NewProduct1 description"
new_product_one.price = 2.5
new_product_one.stock_quantity = 13
new_product_one.category_id = 1
new_product_one.save
puts new_product_one.inspect

# W2

new_product_two = Product.new( 
                      name:  "NewProduct2",
                      description: "NewProduct2 description",
                      price:  3.5,
                      stock_quantity:  55 ,
                      category_id:  1
                    )
new_product_two.save


# W3
new_product_three = Product.create(
  name:  "NewProduct3",
  description: "NewProduct3 description",
  price:  5.5,
  stock_quantity:  41,
  category_id:  1
  )

# show error
new_product_four = Product.new( name: "NewProduct4" )


if (new_product_four.save)
  puts "new_product_four was saved to the database product table."
  puts new_product_four.inspect
else
  puts "There was an error saving new_product_four to the database."
  

  new_product_four.errors.messages.each do |column, errors|
    errors.each do |error|
      puts "The #{column} property #{error}."
    end
  end
end