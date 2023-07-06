def season(month):
    if 3 < month <= 5: return "Spring"
    if 6 < month <= 8: return "Summer"
    if 9 < month <= 11: return "Autumn"
    if 0 < month <= 12: return "Winter"
    else : return "There is no such month"
print(season(10))