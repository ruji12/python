
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
