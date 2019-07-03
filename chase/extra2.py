def main():
    day=int(input("please enter the day of a date"))
    mounth=int(input("please enter the mounth of a date"))
    year=int(input("please enter the year of a date"))
    jijidoji_is_crazy=day*mounth
    jijidoji_is_so_crazy=year-year//100*100
    if(jijidoji_is_crazy==jijidoji_is_so_crazy):
        print("this is a magic day")
    else:
        print("this is not a magic day")
main()
