
def analyzer(data):

    def daily_total():
        grouped_date = {}

        for x in data:
            date = x["Date"]
            amount = x["Amount"]

            if date not in grouped_date:
                grouped_date[date] = []
            grouped_date[date].append(amount)
            
        for date, amounts in grouped_date.items():
            tosum = sum(amounts)
            print("Your total spent money at", date, "is: ", round(tosum, 2))

        return grouped_date
    

    def monthly_total():
        grouped_date = {}

        for x in data:
            date = x["Date"]
            amount = x["Amount"]

            split = date.split(".")
            split.pop(0)
            separator = "."
            month = separator.join(split)
            date = month

            if date not in grouped_date:
                grouped_date[date] = []

            grouped_date[date].append(amount)

        for date, amounts in grouped_date.items():
            tosum = sum(amounts)
            print("Your total spent money at", date, "is: ", round(tosum, 2))
        return grouped_date
    
    # daily_total()
    print("===========================")
    # monthly_total()



    def category():
        grouped_category = {}

        for x in data:
            category = x["Category"]

            amount = x["Amount"]

            if category not in grouped_category:
                grouped_category[category] = []
            grouped_category[category].append(amount)

        for category, amounts in grouped_category.items():
            tosum = sum(amounts)
            print("Twoje wydatki na", category.lower(), "wyniosły: ", round(tosum, 2))

        return grouped_category
    
    # category()

    def monthly_category():
        monthly_category = {}

        for x in data:
            date = x["Date"]
            category = x["Category"]
            amount = x["Amount"]
            split = date.split(".")
            split.pop(0)
            separator = "."
            month = separator.join(split)
            date = month

            if (date, category) not in monthly_category:
                monthly_category[date, category] = []
            monthly_category[date, category].append(amount)

        for (date, category), amounts in monthly_category.items():
            tosum = sum(amounts)
            print("Twoje wydatki na", category.lower(), "w miesiącu", date, "wyniosły: ", round(tosum, 2))

        return monthly_category
        
    monthly_category()


    return data
    
