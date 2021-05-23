# random-uuid
end point generates a random uuid anything it's called. ordering is from latest to oldest

# Data
you can load initial data into your db by simply doing `python manage.py loaddata fixtures/initial.json --app uuid_generator.RandomGenerator`

# Test
test can be run by simply typing `pytest` , however tests are setup to run on every push. 
