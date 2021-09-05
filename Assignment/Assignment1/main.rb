# Qingbei Huang/Assginment1 of Full-Stack WebDev

# ask user to enter the subtotal
puts("Please enter your subtotal")

# define necesarry variables
sub_total = gets.chomp.to_f #convert into float before using it
GST = 0.05
PST = 0.07
grand_total = 0

# define a method to convet GST&PST into percentage format
def num_to_percentage(num)
  return (num*100).to_s+'%'
end
#define a method to culculate grand total
def grand_total_cul(sub,gst,pst)
  return sub+((sub*gst)+(sub*pst))
end
#define a method to culculate gst 
def gst_cul(sub,gst)
  return (sub*gst)
end
#define a method to culculate pst
def pst_cul(sub,pst)
  return (sub*pst)
end
#define a variable to store short message after grand total
short_message = if grand_total_cul(sub_total,GST,PST) <= 5
  "Pocket Change"
elsif  grand_total_cul(sub_total,GST,PST) > 5 && grand_total_cul(sub_total,GST,PST) <20
  "Wallet Time"
elsif grand_total_cul(sub_total,GST,PST) >= 20
  "Charge It!"
end
puts("Subtotal: $#{sub_total}
PST: $#{pst_cul(sub_total,PST)} - #{num_to_percentage(PST)}
GST: $#{gst_cul(sub_total,GST)} - #{num_to_percentage(GST)}
Grand Total: $#{grand_total_cul(sub_total,GST,PST)}
#{short_message}")
