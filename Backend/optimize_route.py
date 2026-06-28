import sys
import json
from geopy.distance import great_circle
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def create_data_model(distance_matrix):
    data = {}
    data['distance_matrix'] = distance_matrix
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data

def compute_distance_matrix(waypoints):
    num_waypoints = len(waypoints)
    distance_matrix = [[0] * num_waypoints for _ in range(num_waypoints)]
    for i in range(num_waypoints):
        for j in range(num_waypoints):
            if i != j:
                distance_matrix[i][j] = great_circle(waypoints[i], waypoints[j]).meters
    return distance_matrix

def main():
    # Read waypoints from command-line arguments
    waypoints = json.loads(sys.argv[1])
    # Compute distance matrix
    distance_matrix = compute_distance_matrix(waypoints)
    data = create_data_model(distance_matrix)

    # Create the routing index manager
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])
    
    # Create Routing Model
    routing = pywrapcp.RoutingModel(manager)

    # Define cost of each arc
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Set parameters
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution
    if solution:
        output = {'routes': []}
        for vehicle_id in range(data['num_vehicles']):
            index = routing.Start(vehicle_id)
            route = []
            while not routing.IsEnd(index):
                route.append(manager.IndexToNode(index))
                index = solution.Value(routing.NextVar(index))
            route.append(manager.IndexToNode(index))  # Add end node
            output['routes'].append(route)
        print(json.dumps(output))  # Ensure valid JSON output
    else:
        print(json.dumps({'error': 'No solution found'}))

if __name__ == '__main__':
    main()
