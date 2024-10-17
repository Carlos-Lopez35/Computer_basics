#preguntar la posición original, velocidad original, aceleración y momento en el que se quiere conocer la posición 
original_position= float(input ("Please, tell me the original position of the object on the x axis in meters."))
original_velocity=float( input ("Please, tell me the original velocity of the object in meters per second."))
acceleration= float(input ("Please, tell me the acceleration of the object in meters per square seconds."))
time= float(input("Please, tell me the a time in seconds for which you want to know the position and the velocity."))
#calcular la velocidad final
final_velocity= original_velocity + acceleration * time
print ("The velocity in second",time, "is" ,final_velocity,"m/s.")
#calcular la posición final
final_position= (original_position + original_velocity * time + (acceleration * time ** 2) / 2)
print ("The position in second ",time,"is",final_position,"m." )
print("Acceleration is constant, because no force is applied to the object.")