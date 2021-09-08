#Qingbei Huang challenge 2
require 'net/http'
require 'json'
require 'pp'
# Using a single puts statement build the following
# sentence using only data from the carl hash and the
# sagan array along with some string interpolation.
#
# We are a way for the cosmos to know itself.
#Q1
carl  = {
  :toast => 'cosmos',
  :punctuation => [ ',', '.', '?' ],
  :words => [ 'know', 'for', 'we']
}

sagan = [
  { :are => 'are', 'A' => 'a' },
  { 'waaaaaay' => 'way', :th3 => 'the' },
  'itself',
  { 2 => ['to']}
]

puts "#{carl[:words][2]} #{sagan[0][:are]} #{sagan[0]['A']} #{sagan[1]['waaaaaay']} #{carl[:words][1]} #{sagan[1][:th3]} #{carl[:toast]} #{sagan[3][2][0]} #{carl[:words][0]} #{sagan[2]}"

#Q2
ghosts = [{:name=>'Inky',:loves=>'reinderrs',:age=>"4",:net_worth=>"25"},
  {:name=>'Pinky',:loves=>'garden tools',:age=>"5",:net_worth=>"14"},
  {:name=>'Blinky',:loves=>'ninjas',:age=>"7",:net_worth=>"18.03"},
  {:name=>'Clyde',:loves=>'yarn',:age=>"6",:net_worth=>"0"}]
ghosts.each do |ghost|
  ghost_info  = "#{ghost[:name]} is #{ghost[:age]} years old, "
  ghost_info += "loves #{ghost[:loves]} and "
  ghost_info += "has #{ghost[:net_worth]} dollars in the bank."
  puts ghost_info
end

#Q3

 
url = 'https://dog.ceo/api/breeds/list/all'
uri = URI(url)
response = Net::HTTP.get(uri)
dog_breeds = JSON.parse(response) # Convert JSON data into Ruby data.
dog_breeds_list = dog_breeds['message'] 
dog_breeds_list.each do |key,value|
  puts "* #{key}"
  value.each do |sub|
    puts " * #{sub}"
  end
end

#Q4
urlTree = 'https://data.winnipeg.ca/resource/d3jk-hb6j.json?$limit=306000'
uriTree = URI(urlTree)
responseTree = Net::HTTP.get(uriTree)
trees = JSON.parse(responseTree)
# puts trees
ashTrees = 0;
trees.each do |tree|
  if tree['common_name'].include? "ash"
    ashTrees += 1
  end
end
puts ashTrees