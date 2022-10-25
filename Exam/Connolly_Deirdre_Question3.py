# Name:         Deirdre Connolly
# Student ID:   R00112962


def read_sales_data():
    file = open("sales.txt")
    sales = file.readlines()
    sales_list = []
    for i in range(len(sales)):
        sales_list.append(int(sales[i]))
    print(sales_list)
    file.close()
    return sales_list


def show_weekly_stats(read_sales_data):
    sales_list = read_sales_data()
    average = (sum(sales_list) / len(sales_list))
    print("The average sales for the week was " + str(average) + ".")


show_weekly_stats(read_sales_data)



