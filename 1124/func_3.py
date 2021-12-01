def do_anything(*args):
    print("受け取った値：",args)
    if len(args)==0:
        print("やること無いので暇です")

    elif len(args)==1:
        if type(args[0]) is str or str(args[0]).isdigit():
            print(args[0]*2)
        else:print("難しくて無理です")

    elif len(args)==2:
        if not(isinstance(args[0],(str,int)) or isinstance(args[1],(str,int))):
            print("無茶言わないで！")
        elif type(args[0])==type(args[1]):
            print(args[0]+args[1])
        else:print("できません〜")

    else:print("無理です…")

# main
do_anything()
do_anything(10)
do_anything('asdfg')
do_anything([1,2,3])
do_anything(10,20)
do_anything(10,'abc')
do_anything('x','yz')
do_anything([1,2,3],[4,5,6])
do_anything(1,2,3)