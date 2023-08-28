# Phase 3 ORM Challenge - Animal Zoo

For this mock challenge, we'll be working with a domain for a zoo.

We have one model: `Animal` which shows the animals who occupy our zoo.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- lists and list Methods
- SQL queries
- ORM methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Your tables have not been created yet. In order to build them, first use
`python debug.py` and then use the class method `Show.create_table()`.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects. There are no formal tests to run with this code so be
sure to test it in the `debug.py` often.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers and Properties

- `Animal __init__(name, age, id=None)`
  - `Animal` is initialized with a name (string) and an age (integer)
  - When initialized an Animal should have an id of None
  - Assume that Animals will always be initialized with the proper data types
- `Animal __repr__()`
  - Returns the Animal instance in the format below:
  - `Animal(id={id} name={name}, age={age})`
- `Animal property age()`
  - Returns the `Animal`'s age
  - Age must be an integer greater than 0

### SQL Methods

- `Animal create()`
  - Creates an Animal in the database with the instance's attributes
- `Animal update()`
  - Updates an Animal in the database based on the instance's attributes
- `Animal save()`
  - Will either create or update the Animal in the database depending on whether the Animal has an id
- `Animal delete()`
  - Deletes the Animal from the database
  - No return value is necessary for this method
- `Animal classmethod query_all()`
  - Returns a list of Animal instances based on rows in the database
  - The return value ought to be a list of Animal instances

### BONUS Methods

- `Animal classmethod query_oldest()`
  - Returns the oldest Animal by age from the database as an instance
- `Animal classmethod average_age()`
  - Returns the average age of animals in the database
- `Animal happy_birthday()`
  - Updates both the database and the Animal instance by incrementing the age by one
