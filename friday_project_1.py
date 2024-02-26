a_large_object = input("Enter a large object: ")
large_objects_plural = input("Enter a large object (plural): ")
an_adjective = input("Enter an adjective: ")
a_body_part = input("Enter a body part: ")
a_restaurant = input("Enter a restaurant: ")
a_food = input("Enter a food: ")
another_food = input("Enter another food: ")

madlib = f'''I have had a very {an_adjective} day.
This morning, I dropped a box of {large_objects_plural} on my {a_body_part}.
Then, at lunch, I went to {a_restaurant} for their delicious {a_food},
But the waiter brought me {another_food}, which I was not hungry for.
Finally, on my way home, I was cut off by a van with a large {a_large_object} strapped to the roof.'''

print(madlib)