require_relative 'ar.rb'


for value in (1..10) do
  new_category = Category.create( 
      name: Faker::Food.unique.fruits
    )
    puts new_category.id
  for value in (1..10) 
    new_product = Product.create( 
      name:  Faker::Food.unique.spice,
      description: Faker::Mountain.name,
      price:  Faker::Number.decimal(l_digits: 2),
      stock_quantity:  Faker::Number.number(digits: 2) ,
      category_id: new_category.id
    )
    puts new_product.category_id
  end
end