from module_6_functions.classes.class_folder.my_classes import Car

my_car = Car(make='Ford', model="f150", year=2012, mileage=160000, color='Blue', condition='Used')

#print(my_car) # returns object
#print(my_car.make) # returns make
#print(my_car.__dict__) # shows all properties

my_wifes_car = Car(make='Toyota', model="Avalon", year=2005, mileage=86550, color='Pearl White', condition='Used')

print(my_wifes_car.__dict__)