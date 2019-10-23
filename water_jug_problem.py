from collections import defaultdict 

visited = defaultdict(lambda: False) 
jug1_capacity, jug2_capacity, aim = 4, 3, 2

def waterJugSolver(action,jug1,jug2):
    if (jug1 == aim): 
        print("end of the steps",jug1, jug2) 
        return True

    if visited[(jug1, jug2)] == False: 
        print(action,jug1, jug2) 

        visited[(jug1, jug2)] = True

        return (waterJugSolver(">Pour jug1<        ",0, jug2) or
                waterJugSolver(">Pour jug2<        ",jug1, 0) or
                waterJugSolver(">Fill jug1<        ",jug1_capacity, jug2) or
                waterJugSolver(">Fill jug2<        ",jug1, jug2_capacity) or
                waterJugSolver(">From jug2 to jug1<",jug1 + min(jug2, (jug1_capacity-jug1)), jug2 - min(jug2, (jug1_capacity-jug1))) or
                waterJugSolver(">From jug1 to jug2<",jug1 - min(jug1, (jug2_capacity-jug2)),  jug2 + min(jug1, (jug2_capacity-jug2)))) 
    else:
        return False

print("Steps: ") 
waterJugSolver(">Initial state is< ",0, 0) 