#This is a rudimentary neural network. I believe that I could solve more difficult problems by following the same format. 
import Random

n1 = [Random.rand,Random.rand]
n2 = [Random.rand,Random.rand]
neurons= [n1, n2]
trainingSet = input("How many training vectors would you like to input?")

for i in range(0,int(trainingSet)):
    trainingVector = list(input("Input a vector without brackets"))
    trainingSolution = list(input("Input the desired solution (In the same form, orthonormal)."))
    
for neuron in range(2):
    for weight in range(2):
        neurons[neuron][weight]+= int(trainingSolution[neuron])*int(trainingVector[weight])
        #Chooses the neuron and the weight          Training solution must depend on neuron, as the neurons are the basis of the output.

  
print(neurons)            
            
            
    


        
