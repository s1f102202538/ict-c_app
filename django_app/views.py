from django.shortcuts import render

def check_date_and_name(request):
    dataList = [
        { "date": "2023-08-30", "name": "Alice" },
        { "date": "2023-08-29", "name": "Bob" },
        { "date": "2023-08-28", "name": "Charlie" }
    ]
    
    if request.method == "POST":
        dateInput = request.POST.get("dateInput")
        nameInput = request.POST.get("nameInput")
        
        matchingData = next((item for item in dataList if item["date"] == dateInput), None)
        
        if matchingData:
            result = f"{nameInput}さんは{matchingData['name']}さんとマッチしました❤"
        else:
            result = "残念ですが、誰ともマッチしませんでした"
        
        return render(request, "date_matching.html", {"result": result})
    
    return render(request, "date_matching.html", {"result": ""})
