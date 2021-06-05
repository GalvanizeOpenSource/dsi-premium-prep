def mean(lst, trim_by=0):
    lst_ = lst.copy()
    
    if trim_by > 0:
        lst_ = sorted(lst_)[trim_by: -trim_by]
    
    return sum(lst_) / len(lst_)

a = [1, 5, 7, 10, 15, 23, 35, 67, 220, 2000]

# print(mean(a, trim_by=1))


urban = [6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0]
farmhouse = [4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0, 0.3]

# print(f'Sample Mean Urban: {round(mean(urban), 1)}')
# print(f'Sample Mean Farmhouse: {round(mean(farmhouse), 1)}')

# print()

# print(f'Trimmed Sample Mean Urban: {round(mean(urban, trim_by=1), 1)}')
# print(f'Trimmed Sample Mean Farmhouse: {round(mean(farmhouse, trim_by=1), 1)}')



def median(lst):
    lst_ = sorted(lst)

    if len(lst) % 2:
        mid_idx = int(len(lst) / 2)
        return lst_sorted[mid_idx]



odd_list = [13, 18, 13, 14, 13, 16, 14, 21, 13]
even_list = [15, 14, 10, 8, 12, 8, 16, 13]

print(median(odd_list))
print(median(even_list))