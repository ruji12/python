#nesting dictionary  and lists in a dictionary .
# travel_log={
#     "France":{"cities_visited":["paris","lille","Dijon"],"total_visit":23},
#     "Germany":{"cities_visited":["Berlin","stugart","hamburg"],"total_visited":18},
# }

# print(travel_log)
# #nesting a dictionary inside a list.
#syntax
# [{
#     key:[list],
#     key2:{Disct},
# } ,
# {
#     key:value,
#     key2:value,
# }

# ]
#nesting dictionary in a lists

travel_log=[{
            "country":"France",
             "cities_visited":["paris","lille","Dijon"],
             "total_visit":23
             },
           {
            "country":"Germany",
            "cities_visited":["Berlin","stugart","hamburg"],
            "total_visited":18
            },

]

def add_new_country(country,total_visited,cities_visited):
    my_travel={
        "country":country,
        "total_visited":total_visited,
        "cities_visited":cities_visited,
    }
    travel_log.append(my_travel)

add_new_country("Russia",2,["Moscow","saint peterbus"])
print(travel_log)
