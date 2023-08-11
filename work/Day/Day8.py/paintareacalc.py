#You are painting a wall.the instruction on the paint can says that 1 can of paint can cover 5 square meters of wall.Given a random height and width of wall.calculate how many cans of paint you'll need to buy.

# number of cans = (wall height*wall width)/coverage per can

# h=2,w=4,c=5
height=int(input("enter the height of the wall."))
width=int(input("enter the height of the wall."))
coverage=5
def calc(h,w,cov):
    num_of_cans=(float)(h*w)/cov
    rounded_num=round(num_of_cans)
    print(f"number of cans required are { rounded_num}")



calc(height,width,coverage)




