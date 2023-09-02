from django.shortcuts import render

def check_date_and_name(request):
    dataList = [
    { "date": "2023-08-01", "name": "坂村健" },
    { "date": "2023-08-02", "name": "井上円了" },
    { "date": "2023-08-30", "name": "Alice" },
    { "date": "2023-08-30", "name": "ooo" },
    { "date": "2023-08-29", "name": "Bob" },
    { "date": "2023-08-28", "name": "Charlie" },
    { "date": "2023-08-27", "name": "David" },
    { "date": "2023-08-26", "name": "Eva" },
    { "date": "2023-08-25", "name": "Frank" },
    { "date": "2023-08-24", "name": "Grace" },
    { "date": "2023-08-23", "name": "Henry" },
    { "date": "2023-08-22", "name": "Ivy" },
    { "date": "2023-08-21", "name": "Jack" },
    { "date": "2023-08-20", "name": "Karen" },
    { "date": "2023-08-19", "name": "Leo" },
    { "date": "2023-08-18", "name": "Mia" },
    { "date": "2023-08-17", "name": "Nathan" },
    { "date": "2023-08-16", "name": "Olivia" },
    { "date": "2023-08-15", "name": "Paul" },
    { "date": "2023-08-14", "name": "Quinn" },
    { "date": "2023-08-13", "name": "Rachel" },
    { "date": "2023-08-12", "name": "Samuel" },
    { "date": "2023-08-11", "name": "Tina" },
    { "date": "2023-08-10", "name": "Ulysses" },
    { "date": "2023-08-09", "name": "Victoria" },
    { "date": "2023-08-08", "name": "William" },
    { "date": "2023-08-07", "name": "Xander" },
    { "date": "2023-08-06", "name": "Yara" },
    { "date": "2023-08-05", "name": "Zane" },
]
    
    if request.method == "POST":
        dateInput = request.POST.get("dateInput")
        nameInput = request.POST.get("nameInput")
        
        matchingData = [item for item in dataList if item["date"] == dateInput]
        
        if matchingData:
            matching_names = ", ".join(item["name"] + "さん" for item in matchingData)  # ここを変更
            result = f"{nameInput}さんは{matching_names}とマッチしました❤"
        else:
            result = f"{nameInput}さん、誰ともマッチしませんでした😢"
        
        return render(request, "django_app/date_matching.html", {"result": result})
    
    return render(request, "django_app/date_matching.html", {"result": ""})

