import random
import matplotlib.pyplot as plt
import json


# Implementing a race car
class RaceCar:

    def __init__(self, start_position):
        self._speed = [0, 0]
        self._position = start_position

    def getSpeed(self):
        return self._speed

    def getPosition(self):
        return self._position

    # Calculate the trajectory given initial position and speed
    def trajectory(self):
        s = self._speed
        p = self._position
        trajectory_from_p = []
        for i in range(1, 1 + s[0]):
            vertical_displacement = i * s[1] / s[0]

            if (i * s[1]) % s[0] == 0:
                trajectory_from_p.append([p[0] + i, p[1] + int(vertical_displacement)])
            else:
                trajectory_from_p.append([p[0] + i - 1, p[1] + int(vertical_displacement)])
                trajectory_from_p.append([p[0] + i, p[1] + int(vertical_displacement)])

        for i in range(1, 1 + s[1]):
            horizontal_displacement = i * s[0] / s[1]

            if (i * s[0]) % s[1] != 0:
                if [int(p[0] + horizontal_displacement), p[1] + i] not in trajectory_from_p:
                    trajectory_from_p.append([int(p[0] + horizontal_displacement), p[1] + i])
                if [int(p[0] + horizontal_displacement), p[1] + i - 1] not in trajectory_from_p:
                    trajectory_from_p.append([int(p[0] + horizontal_displacement), p[1] + i - 1])

        trajectory_from_p.sort(key=lambda x: ((x[0] - p[0]) ** 2 + (x[1] - p[1]) ** 2) ** 0.5)
        return trajectory_from_p
    
    def possible_acceleration(self):
        possibilities = []
        for i in range(3):
            for j in range(3):
                if ((5 >= self._speed[0] + i - 1 >= 0) and (5 >= self._speed[1] + j - 1 >= 0) and
                    ((self._speed[0] + i - 1 != 0) or (self._speed[1] + j - 1 != 0))):

                    possibilities.append([i - 1, j - 1])

        return possibilities

    def move(self):
        self._position[0] += self._speed[0]
        self._position[1] += self._speed[1]

    def accelerate(self, a):
        self._speed[0] += a[0]
        self._speed[1] += a[1]

    def replace(self, position):
        self._position = position
        self._speed = [0, 0]


# Implementing a map for the track
class RoadMap:

    def __init__(self, RoadBoundary_Matrix, starting_line, finishing_line):
        self._map = RoadBoundary_Matrix
        self._start = starting_line
        self._finish = finishing_line

    def out(self, position):
        if position not in self._map:
            return True

    def finish(self, position):
        if position in self._finish:
            return True

    def random_start_point(self):
        return random.choice(self._start).copy()

    def getMap(self):
        return self._map


# Implementing On-Policy First-Visit Monte Carlo method
class On_Policy_First_Visit_Monte_Carlo:

    def __init__(self, RoadBoundary_Matrix, starting_line, finishing_line):
        self._roadmap = RoadMap(RoadBoundary_Matrix, starting_line, finishing_line)
        self._car = RaceCar(self._roadmap.random_start_point())
        self._q = {}
        self._Return = {}
        self._policy = {}
        self._epsilon = 0.15

    def getPolicy(self):
        return self._policy

    def update_q(self, nodes):
        for node in nodes:
            r = self._Return[node]
            self._q[node] = sum(r)/len(r)

    def update_Return(self, nodes, reward):
        for node in nodes:
            self._Return[node].append(reward)

    def action(self):
        possible_action = self._car.possible_acceleration()
        n = len(possible_action)
        old_position = self._car.getPosition().copy()
        old_speed = self._car.getSpeed().copy()

        if random.random() < 0.9:
            state_action = [[old_position, old_speed, a] for a in possible_action]
            for sa in state_action:
                if repr(sa) not in self._q:
                    self._q[repr(sa)] = 0
            maximum_q = max([self._q[repr(sa)] for sa in state_action])
            optimal_actions = []
            for sa in state_action:
                if self._q[repr(sa)] == maximum_q:
                    optimal_actions.append(sa)
            optimal_action = random.choice(optimal_actions)
            self._policy[repr([sa[0], sa[1]])] = optimal_action[2]

            if random.random() < 1 - self._epsilon:
                a = optimal_action[2]
            else:
                a = random.choice(state_action)[2]
            optimal_action[2] = a

            if repr(optimal_action) not in self._Return:
                self._Return[repr(optimal_action)] = []

        else:
            a = [0, 0]
            sa = repr([old_position, old_speed, [0,0]])
            if sa not in self._q:
                self._q[sa] = 0
                self._Return[sa] = []

        self._car.accelerate(a)
        trajectory = self._car.trajectory()
        self._car.move()

        return [old_position, old_speed, a], trajectory

    def episode(self):
        reward = 0
        states = list()
        while True:
            # print(self._car.getPosition())
            # print(self._car.getSpeed())
            # print()
            reward -= 1
            action = self.action()
            if repr(action[0]) not in states:
                states.append(repr(action[0]))
            new_pos = self._car.getPosition()
            for trajectory in action[1]:
                if self._roadmap.finish(trajectory):
                    self._car.replace(self._roadmap.random_start_point())
                    for i in states:
                        if i not in self._Return:
                            self._Return[i] = []
                    self.update_Return(states, reward)
                    self.update_q(states)
                    return reward
                elif self._roadmap.out(trajectory):
                    self._car.replace(self._roadmap.random_start_point())
                    break
    

# Build the map
Turn = []
for i in range(10):
    for j in range(30):
        Turn.append([i+10, j])
for i in range(10):
    for j in range(10):
        Turn.append([i + 20, j + 20])
StartLine = [[i+10, 0] for i in range(10)]
FinishLine = [[29, j + 20] for j in range(10)]


if __name__ == '__main__':

    simulations = []
    average_reward = []

    for i in range(50):
        simulations.append(On_Policy_First_Visit_Monte_Carlo(Turn, StartLine, FinishLine))
    for i in range(1000):
        rewards = []
        for j in range(50):
            r = simulations[j].episode()
            rewards.append(r)
        average_reward.append(sum(rewards)/len(rewards))
    print(average_reward)
    Xaxis = [1, 3, 5, 7] + [10 * i for i in range(1,100)]
    Yaxis = [average_reward[i] for i in Xaxis]
    plt.plot(Xaxis, Yaxis)
    plt.xlabel('number of steps')
    plt.ylabel('Average rewards')
    plt.legend()
    plt.show()

    # To check what policy does the agent find
    find_optimal_policy = On_Policy_First_Visit_Monte_Carlo(Turn, StartLine, FinishLine)
    for i in range(10000):
        find_optimal_policy.episode()
    policy = find_optimal_policy.getPolicy()
    print(policy)
    start_point = '[[10, 0], [0, 0]]'
    #start_point = '[[14, 0], [0, 0]]'
    #start_point = '[[19, 0], [0, 0]]'

    next_point = start_point
    while next_point in policy:
        print(next_point, policy[next_point])
        n = json.loads(next_point)
        position = n[0]
        speed = n[1]
        action = policy[next_point]
        speed[0] += action[0]
        speed[1] += action[1]
        position[0] += speed[0]
        position[1] += speed[1]
        next_point = repr([position,speed])

