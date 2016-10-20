def volume(H,L,W):
    return (H*L*W)
h = int(input("height of the box:"))
l = int(input("length of the box:"))
w = int(input("width of the box:"))

print("Volume of box is", volume(h,l,w)/(1728))

