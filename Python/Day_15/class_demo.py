class Person:

    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    
    def __init__(self, title, name, surname):
        if title not in self.TITLES:
            raise ValueError("%s is not a valid title." % title)
        self.title = title
        self.name = name
        self.surname = surname

    def __str__(self):
        return "Title: %s, Name: %s, Surname %s" % (self.title, self.name, self.surname)


    # def fullname(self):
    #     if hasattr(self, "_fullname"):
    #         return self._fullname
    #     fullname = "%s %s" % (self.name, self.surname)
    #     self._fullname = fullname
    #     return fullname

    @property
    def fullname(self):
        return "%s %s" % (self.name, self.surname)


    @fullname.setter
    def fullname(self, value):
        name, surname = value.split(" ",1)
        self.name = name
        self.surname = surname


    @fullname.deleter
    def fullname(self):
        del self.name
        del self.surname


    @classmethod
    def allowed_titles_starting_with(cls, startswith):
        # class instance is accessible through cls
        return [title for title in cls.TITLES if title.startswith(startswith)]


    @staticmethod
    def allowed_titles_ending_with(endswith):
        # no parameter for class or instance object
        # we have to use Person directly
        return [title for title in Person.TITLES if title.endswith(endswith)]


person_object = Person(
    "Mr",
    "John",
    "Smith"
)

print(person_object.name)
print(person_object.surname)
# print(person_object.fullname())
import pdb; pdb.set_trace()
print(person_object.fullname)  # no brackets

print(person_object.allowed_titles_starting_with("M"))
print(Person.allowed_titles_starting_with("M"))

print(person_object.allowed_titles_ending_with("s"))
print(Person.allowed_titles_ending_with("s"))