
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
    
    daily_total()
    print("===========================")
    monthly_total()
    return data
    
