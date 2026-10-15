EXERCISES = {
1: r'''
EXERCISE 1 — DEPTH FIRST SEARCH (DFS)
# Practical code
graph = {
    'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'],
    'D': [], 'E': ['F'], 'F': []
}

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print("Visited:", node)
            visited.add(node)
            # Reverse preserves the listed neighbor order during traversal.
            stack.extend(reversed([n for n in graph.get(node, []) if n not in visited]))

dfs(graph, 'A')

HOMEWORK 1 — MAZE-SOLVING GAME
# Each walkable tile is a node; edges connect walkable neighboring tiles.
maze_graph = {
    (0, 0): [(0, 1)], (0, 1): [(0, 0), (1, 1)],
    (1, 1): [(0, 1), (1, 2)], (1, 2): [(1, 1), (2, 2)],
    (2, 2): [(1, 2)]
}
def maze_dfs(graph, start, exit_tile):
    stack = [(start, [start])]
    visited = set()
    while stack:
        node, path = stack.pop()
        if node == exit_tile:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return None
print("Maze exit path:", maze_dfs(maze_graph, (0, 0), (2, 2)))

maze={'S':['A'],'A':['B'],'B':['C'],'C':['E'],'E':[]}

def dfs(g,s,e):
    v=set(); st=[s]
    while st:
        n=st.pop()
        if n not in v:
            print("Visited:",n); v.add(n)
            if n==e:
                print("Exit found!")
                break
            st+=g[n]


dfs(maze,'S','E')



HOMEWORK 2 — E-COMMERCE CATEGORY CRAWLER
# Demonstration with a category tree (use approved URLs/data in a real crawler).
categories = {
    "Home": ["Electronics", "Clothing"],
    "Electronics": ["Phones", "Laptops"],
    "Phones": ["Android", "iOS"],
    "Android": ["Accessories"],
    "Accessories": [],
    "iOS": [], "Laptops": [], "Clothing": []
}
def crawl_categories(tree, root):
    stack, visited = [root], set()
    while stack:
        category = stack.pop()
        if category in visited:
            continue
        visited.add(category)
        print("Scraped category:", category)
        stack.extend(reversed(tree.get(category, [])))
crawl_categories(categories, "Home")
''',
2: r'''
EXERCISE 2 — BFS SHORTEST PATH
from collections import deque
graph = {
    'A': ['B', 'C'], 'B': ['A', 'D', 'E'],
    'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']
}
def bfs_shortest_path(graph, start, goal):
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None
print("Shortest path:", bfs_shortest_path(graph, 'A', 'F'))

HOMEWORK 1 — CAMPUS DELIVERY ROUTE
campus = {
    "Main_Gate": ["Library", "Canteen"],
    "Library": ["Main_Gate", "IT_CS_Building"],
    "Canteen": ["Main_Gate", "Auditorium"],
    "Auditorium": ["Canteen", "IT_CS_Building"],
    "IT_CS_Building": ["Library", "Auditorium"]
}
print("Campus route:", bfs_shortest_path(campus, "Main_Gate", "IT_CS_Building"))

HOMEWORK 2 — SOCIAL NETWORK DEGREES
social = {
    "Asha": ["Ravi", "Mina"], "Ravi": ["Asha", "Dev"],
    "Mina": ["Asha", "Leena"], "Dev": ["Ravi"], "Leena": ["Mina"]
}
def connection_degree(graph, start, target):
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        person, degree = queue.popleft()
        if person == target:
            return degree
        for friend in graph.get(person, []):
            if friend not in visited:
                visited.add(friend)
                queue.append((friend, degree + 1))
    return None
print("Asha to Dev degree:", connection_degree(social, "Asha", "Dev"))
''',
3: r'''
EXERCISE 3 — N-QUEEN BACKTRACKING
def solve_n_queens(n):
    solutions = []
    def solve(row, board):
        if row == n:
            solutions.append(board.copy())
            return
        for col in range(n):
            safe = all(
                col != old_col and abs(row - old_row) != abs(col - old_col)
                for old_row, old_col in enumerate(board)
            )
            if safe:
                solve(row + 1, board + [col])
    solve(0, [])
    return solutions

for solution in solve_n_queens(4):
    print("Queen columns by row:", solution)

HOMEWORK 1 — EXAM HALL SEATING
# Model one seat per row; students taking the same paper cannot share
# a column or diagonal. This is the N-Queen constraint model.
n = 4
print("Valid seating layouts:", solve_n_queens(n))

HOMEWORK 2 — WAREHOUSE DRONE NODES
# If a row has no safe column, solve() returns from that recursive call.
# The caller then removes its last placement implicitly by trying the next
# column in its loop (backtracking).
print("When row 3 has no safe column, backtrack to row 2 and try its next column.")
---
N=4
def solve(r=0,b=[]):
    if r==N: print("Drone Placement:",b); return True
    for c in range(N):
        if all(c!=x and abs(r-i)!=abs(c-x) for i,x in enumerate(b)):
            if solve(r+1,b+[c]): return True
    return False


solve()

''',
4: r'''
EXERCISE 4 — TOWER OF HANOI
def hanoi(n, source, destination, auxiliary):
    if n == 0:
        return
    hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n}: {source} -> {destination}")
    hanoi(n - 1, auxiliary, destination, source)

hanoi(3, 'A', 'C', 'B')

HOMEWORK 1 — ROBOTIC ARM ASSEMBLY LINE
# Exact function call requested by the question:
hanoi(3, 'Tray_A', 'Tray_C', 'Tray_B')
# The three-disk solution makes 7 legal moves.

HOMEWORK 2 — CLOUD BACKUP MIGRATION
def hanoi_move_count(n):
    return 2 ** n - 1
print("Moves for 3 layers:", hanoi_move_count(3))
print("Time complexity: O(2^n); recurrence T(n) = 2*T(n-1) + 1.")
''',
5: r'''
EXERCISE 5 — HILL CLIMBING
import random
def score(x):
    return -((x - 2) ** 2) + 4  # Maximum is at x = 2.

def hill_climb(iterations=100, start=None, step=0.1):
    current = random.uniform(-10, 10) if start is None else start
    for _ in range(iterations):
        neighbor = current + random.uniform(-step, step)
        if score(neighbor) > score(current):
            current = neighbor
    return current, score(current)

best_x, best_score = hill_climb()
print(f"Best x: {best_x:.4f}; score: {best_score:.4f}")

HOMEWORK 1 — E-COMMERCE AD BUDGET TUNING
# Example objective: click-rate score peaks near a budget of 50.
def click_rate(budget):
    return -((budget - 50) ** 2) / 1000 + 5
def optimize_budget(start=20, iterations=100):
    current = start
    for _ in range(iterations):
        neighbor = max(0, current + random.uniform(-5, 5))
        if click_rate(neighbor) > click_rate(current):
            current = neighbor
    return current, click_rate(current)
print("Optimized budget and click-rate score:", optimize_budget())

HOMEWORK 2 — DELIVERY SPEED / LOCAL MAXIMUM
# A local maximum can trap greedy hill climbing. Random restarts try
# different starting speeds; keep the best result across runs.
def random_restart_hill_climb(restarts=10):
    candidates = [hill_climb(iterations=500, start=random.uniform(-10, 10))
                  for _ in range(restarts)]
    return max(candidates, key=lambda item: item[1])
print("Best across restarts:", random_restart_hill_climb())

-----

import random

score=lambda x: -(x-60)**2+100
best=None


for _ in range(10):
    x=random.uniform(30,100)
    for _ in range(100):
        n=x+random.uniform(-1,1)
        if score(n)>score(x): x=n
    if best is None or score(x)>score(best): best=x


print(f"Best Speed: {best:.2f}, Mileage Score: {score(best):.2f}")


''',
6: r'''
EXERCISE 6 — MISSIONARIES AND CANNIBALS
from collections import deque
def valid_state(m, c):
    return 0 <= m <= 3 and 0 <= c <= 3 and (
        m == 0 or m >= c
    ) and (3 - m == 0 or (3 - m) >= (3 - c))

def missionaries_cannibals():
    start, goal = (3, 3, 1), (0, 0, 0)
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        m, c, boat = path[-1]
        if (m, c, boat) == goal:
            return path
        for dm, dc in moves:
            if boat == 1:
                nxt = (m - dm, c - dc, 0)
            else:
                nxt = (m + dm, c + dc, 1)
            nm, nc, _ = nxt
            if valid_state(nm, nc) and nxt not in visited:
                visited.add(nxt)
                queue.append(path + [nxt])
    return None
print("Safe crossing path:", missionaries_cannibals())

HOMEWORK 1 — HAZARDOUS CHEMICAL TRANSPORT
# State = (Chemical_X_on_starting_side, Catalyst_Y_on_starting_side,
#          Cart_on_starting_side: 1 or 0). Reject unsafe states on either dock.
def safe_chemical_state(x, y):
    return (0 <= x <= 3 and 0 <= y <= 3 and
            (x == 0 or x >= y) and (3-x == 0 or (3-x) >= (3-y)))
print("Example state (3, 1, 1) safe:", safe_chemical_state(3, 1))

----

# State: (X, Y, Cart)
queue = [[(3, 3, 1)]]
visited = {(3, 3, 1)}


while queue:
    path = queue.pop(0)
    x, y, cart = path[-1]


    if (x, y, cart) == (0, 0, 0):
        print("Safe Path:", path)
        break


    for dx, dy in [(1,0), (2,0), (0,1), (0,2), (1,1)]:
        if cart:
            nx, ny, nc = x-dx, y-dy, 0
        else:
            nx, ny, nc = x+dx, y+dy, 1


        # Check limits and safety
        if 0 <= nx <= 3 and 0 <= ny <= 3:
            if (nx == 0 or nx >= ny) and (3-nx == 0 or 3-nx >= 3-ny):
                state = (nx, ny, nc)
                if state not in visited:
                    visited.add(state)
                    queue.append(path + [state])


HOMEWORK 2 — SECURE NETWORK ROUTING
# BFS uses a FIFO queue and returns a minimum-crossing safe path in an
# unweighted state graph; DFS may find a valid but longer route first.
print("Preferred strategy: BFS, because it explores states by path length.")


queue = [[(3,3,1)]]
seen = {(3,3,1)}
while queue:
    path = queue.pop(0)
    x,y,b = path[-1]

    if (x,y,b) == (0,0,0):
        print("Shortest Safe Path:", path)
        break


    for dx,dy in [(1,0),(2,0),(0,1),(0,2),(1,1)]:
        nx,ny,nb = (x-dx,y-dy,0) if b else (x+dx,y+dy,1)


        if 0<=nx<=3 and 0<=ny<=3 and \
           (nx==0 or nx>=ny) and (3-nx==0 or 3-nx>=3-ny):
            s = (nx,ny,nb)
            if s not in seen:
                seen.add(s)
                queue.append(path+[s])

''',
7: r'''
EXERCISE 7 — A* SEARCH
import heapq
graph = {
    'A': [('B', 1), ('C', 3)], 'B': [('D', 1), ('E', 5)],
    'C': [('G', 2)], 'D': [('G', 1)], 'E': [('G', 2)], 'G': []
}
heuristic = {'A': 5, 'B': 3, 'C': 2, 'D': 1, 'E': 1, 'G': 0}
def a_star(graph, h, start, goal):
    queue = [(h[start], 0, start, [start])]
    best_cost = {start: 0}
    while queue:
        f, g, node, path = heapq.heappop(queue)
        if node == goal:
            return path, g
        if g != best_cost.get(node):
            continue
        for neighbor, weight in graph.get(node, []):
            new_g = g + weight
            if new_g < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = new_g
                heapq.heappush(queue, (new_g + h[neighbor], new_g,
                                       neighbor, path + [neighbor]))
    return None
print("A* result:", a_star(graph, heuristic, 'A', 'G'))

HOMEWORK 1 — FOOD DELIVERY HEURISTIC
from math import hypot
def euclidean_distance(point, destination):
    return hypot(point[0] - destination[0], point[1] - destination[1])
rider = (2, 3)
customer = (8, 11)
print("Straight-line heuristic:", euclidean_distance(rider, customer))
# On a four-direction grid, Manhattan distance is another common heuristic.

----

import heapq

g={'A':[('B',2),('C',3)],'B':[('G',5)],'C':[('G',3)],'G':[]}
h={'A':6,'B':5,'C':3,'G':0}


def astar(s,e):
    q=[(h[s],0,[s])]
    while q:
        f,c,p=heapq.heappop(q); n=p[-1]
        if n==e: return p
        for x,w in g[n]:
            if x not in p: heapq.heappush(q,(c+w+h[x],c+w,p+[x]))


print("A* Path:",astar('A','G'))

HOMEWORK 2 — OVER-ESTIMATING HEURISTIC
print("An overestimating heuristic is inadmissible and can make A* return a")
print("suboptimal route; it loses the usual optimality guarantee.")

g={'A':[('B',2),('C',3)],'B':[('G',5)],'C':[('G',3)],'G':[]}
h={'A':6,'B':10,'C':7,'G':0}


def astar(s,e):
    q=[(h[s],0,[s])]
    while q:
        f,c,p=q.pop(0); n=p[-1]
        if n==e: return p
        for x,w in g[n]:
            if x not in p: q.append((c+w+h[x],c+w,p+[x]))
        q.sort()


print("A* Path:",astar('A','G'))


''',
8: r'''
EXERCISE 8 — AO* GRAPH SEARCH (SIMPLIFIED COST UPDATE)
# Each node maps to alternatives (OR branches); each branch contains
# required child nodes (AND children) and edge costs.
heuristic = {'A': 1, 'B': 6, 'C': 12, 'D': 10, 'E': 4, 'F': 4, 'G': 5, 'H': 7}
graph = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1)], [('H', 1)]],
    'D': [[('E', 1), ('F', 1)]]
}
def ao_star_cost(node):
    if node not in graph:
        return heuristic[node]
    branch_costs = []
    for branch in graph[node]:
        branch_costs.append(sum(edge + ao_star_cost(child) for child, edge in branch))
    heuristic[node] = min(branch_costs)
    return heuristic[node]
print("Estimated best cost from A:", ao_star_cost('A'))
print("Updated heuristic map:", heuristic)

HOMEWORK 1 — UNIVERSITY APP AND-OR TREE
app_graph = {
    'Project': [[('Android', 0)], [('iOS', 0)]],
    'Android': [[('Frontend_UI', 0), ('Firebase_Setup', 0)]],
    'iOS': [[('iOS_UI', 0), ('iOS_Backend', 0)]]
}
app_h = {'Project': 0, 'Android': 0, 'iOS': 0, 'Frontend_UI': 3,
         'Firebase_Setup': 4, 'iOS_UI': 5, 'iOS_Backend': 5}
print("Tree: Project OR (Android AND [Frontend UI, Firebase]) OR (iOS AND [iOS UI, backend]).")

-----

h={'Project':0,'Android':5,'iOS':12,'Frontend':3,'Firebase':4}
g={'Project':[[('Android',1)],[('iOS',1)]],
   'Android':[[('Frontend',1),('Firebase',1)]]}


def ao(n):
    if n in g:
        c=[sum(h[x]+w for x,w in b) for b in g[n]]
        h[n]=min(c)
        for x,w in g[n][c.index(h[n])]: ao(x)


ao('Project')
print("AO* Cost Map:",h)

HOMEWORK 2 — MANUFACTURING PIPELINE
route_x = 15 + 1       # OR branch edge + route cost
route_y = (6 + 1) + (7 + 1)  # AND branch sums both calibrations and edges
print("Route X cost:", route_x, "Route Y cost:", route_y)
print("Choose Route Y if using the manual's edge-weight convention and comparing totals.")

----

h={'Device':0,'X':15,'Y':0,'C1':6,'C2':7}
g={'Device':[[('X',1)],[('Y',0)]],
   'Y':[[('C1',1),('C2',1)]]}


def ao(n):
    if n in g:
        c=[sum(h[x]+w for x,w in b) for b in g[n]]
        h[n]=min(c)
        for x,w in g[n][c.index(h[n])]: ao(x)


ao('Device')
print("AO* Cost Map:",h)

''',
9: r'''
EXERCISE 9 — DATA PREPROCESSING AND EDA
import pandas as pd
import numpy as np
raw_data = {
    'Age': [23, 29, np.nan, 41, 195, 33, 21, np.nan, 38, 26],
    'Salary': [48000, np.nan, 61000, 82000, 55000, np.nan, 93000, 71000, 50000, 64000],
    'Experience_Years': [1, 5, 8, 12, 2, 6, 15, 9, np.nan, 4]
}
df = pd.DataFrame(raw_data)
print("Missing values before cleaning:\n", df.isnull().sum())
df = df.fillna({
    'Age': round(df['Age'].mean()),
    'Salary': df['Salary'].median(),
    'Experience_Years': df['Experience_Years'].mode()[0]
})
df = df[df['Age'] < 100]
print("Cleaned summary:\n", df.describe())

HOMEWORK 1 — CAMPUS PLACEMENT ANALYTICS
placement = pd.DataFrame({
    'Aptitude_Score': [70, 82, np.nan, 76, 88],
    'Annual_Family_Income': [500000, 650000, np.nan, 900000, 9000000]
})
placement['Aptitude_Score'] = placement['Aptitude_Score'].fillna(
    placement['Aptitude_Score'].mean())
placement['Annual_Family_Income'] = placement['Annual_Family_Income'].fillna(
    placement['Annual_Family_Income'].median())
print(placement)

HOMEWORK 2 — SMART WATCH CLEANER
steps = pd.DataFrame({'Daily_Steps': [5000, np.nan, 999999, 8200, 6400]})
steps = steps[steps['Daily_Steps'] < 100000].copy()
steps['Daily_Steps'] = steps['Daily_Steps'].fillna(steps['Daily_Steps'].mean())
print(steps)
''',
10: r'''
EXERCISE 10 — SIMPLE / MULTIPLE LINEAR REGRESSION

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

from google.colab import files
uploaded=files.upload()

import pandas as pd
df= pd.read_csv()

# 1. Select continuous numerical features (X) and the target variable (y)
X_features = df[['duration', 'days_left']]
y_targets = df['price']


# 2. Segment records into train/test evaluation partitions (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X_features, y_targets, test_size=0.2, random_state=42)


# 3. Instantiate model and run training optimization
reg_model = LinearRegression().fit(X_train, y_train)


# 4. Generate predictions on test data
y_predictions = reg_model.predict(X_test)


# 5. Display model parameters and evaluation metrics
print(f"Intercept Constant Vector (β0): {reg_model.intercept_:.4f}")
print(f"Feature Slope Weight Coefficients (β1, β2): {reg_model.coef_}")
print(f"Mean Squared Error (MSE): {mean_squared_error(y_test, y_predictions):.4f}")
print(f"R2 Determination Score: {r2_score(y_test, y_predictions):.4f}")


# 6. Plot performance against the 'duration' feature
plt.figure(figsize=(8, 5))
plt.scatter(X_test['duration'][:100], y_test[:100], color='blue', alpha=0.6, label='Actual Prices')
plt.scatter(X_test['duration'][:100], y_predictions[:100], color='red', alpha=0.6, label='Predicted Prices')
plt.xlabel('Flight Duration (Hours)')
plt.ylabel('Ticket Price')
plt.title('Flight Price Linear Regression Fit (Sample of 100 Test Points)')
plt.legend()
plt.show()


HOMEWORK 1 — STUDENT EXAM SCORE PREDICTOR
# beta_1 is the expected marks change per extra study hour when mock tests
# are held constant; beta_2 is the expected change per extra mock test,
# holding study hours constant.
X_student = np.array([[1, 0], [2, 1], [3, 1], [4, 2], [5, 3], [6, 3]])
y_marks = np.array([45, 52, 60, 68, 78, 85])
student_model = LinearRegression().fit(X_student, y_marks)
print("beta_1 (study hours), beta_2 (mock tests):", student_model.coef_)

----

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv("student_exam_performance.csv")


X = df[["hours_studied", "attendance_percentage"]]
y = df["exam_score"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LinearRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)


print("Intercept (β0):", round(model.intercept_, 4))
print("Coefficients (β1, β2):", model.coef_)
print("MSE:", round(mean_squared_error(y_test, y_pred), 4))
print("R²:", round(r2_score(y_test, y_pred), 4))


plt.scatter(y_test, y_pred)
plt.xlabel("Actual Exam Score")
plt.ylabel("Predicted Exam Score")
plt.title("Actual vs Predicted Exam Scores")
plt.show()



HOMEWORK 2 — HOUSE RENT MODEL VALIDATION
print("R2 = 0.91 means 91% of target variance is explained by the features.")
print("High MSE means squared prediction errors are large; inspect target units,")
print("outliers, train/test split, and residuals before judging the model.")

----

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# 1. Load data & convert price units to uniform Lakhs
df = pd.read_csv("Mumbai House Prices.csv")
df["price_lakhs"] = df["price"] * df["price_unit"].map({"Cr": 100, "L": 1})


# 2. Filter specifically for Vidyavihar region
v_df = df[df["region"].str.contains("Vidyavihar", case=False, na=False)]
data = v_df if len(v_df) >= 5 else df  # Fallback to full dataset if region sample is too small


# 3. Features & Target
X = data[["area", "bhk"]]
y = data["price_lakhs"]


# 4. Train model & predict
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)


# 5. Output exact metrics
mse = mean_squared_error(y_test, y_pred)
print("Intercept (β0):", round(model.intercept_, 4))
print("Coefficients (β1: Area, β2: BHK):", model.coef_)
print("MSE:", round(mse, 4))
print("RMSE (Lakhs):", round(np.sqrt(mse), 4))
print("R² Score:", round(r2_score(y_test, y_pred), 4))


# 6. Plot graph
plt.scatter(y_test, y_pred)
plt.xlabel("Actual House Price (Lakhs)")
plt.ylabel("Predicted House Price (Lakhs)")
plt.title("Actual vs Predicted House Prices (Vidyavihar)")
plt.show()

''',
11: r'''
EXERCISE 11 — LOGISTIC REGRESSION CLASSIFIER
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

X, y = make_classification(n_samples=200, n_features=4, n_informative=3,
                           n_redundant=1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)
model = LogisticRegression(solver='lbfgs').fit(X_train, y_train)
predictions = model.predict(X_test)
print("Confusion matrix:\n", confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

----

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix


# Ingest Kaggle binary classification dataset fields
df = pd.read_csv('heart.csv')
X_features, y_classes = df.drop(columns=['target']), df['target']


X_train, X_test, y_train, y_test = train_test_split(X_features, y_classes, test_size=0.25, random_state=42)


# Initialize model and train weights using optimization solvers
classifier = LogisticRegression(solver='lbfgs', max_iter=1000).fit(X_train, y_train)
predictions = classifier.predict(X_test)


# Display classification metrics summaries
print("--- Confusion Matrix Output ---\n", confusion_matrix(y_test, predictions))
print("\n--- Model Performance Report Summary ---\n", classification_report(y_test, predictions))


HOMEWORK 1 — COLLEGE EVENT ATTENDANCE
import math
z = 0
probability = 1 / (1 + math.exp(-z))
print("Probability at z=0:", probability)  # 0.5 (50%)

----

import pandas as pd, numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix


# Ingest dataset fields
pd.DataFrame({'Engagement': [-3,-2,-1,0,1,2,3], 'Attended': [0,0,0,1,1,1,1]}).to_csv('college_fest.csv', index=False)
df = pd.read_csv('college_fest.csv')
X_tr, X_te, y_tr, y_te = train_test_split(df[['Engagement']], df['Attended'], test_size=0.25, random_state=42)


# Train model & predict
clf = LogisticRegression().fit(X_tr, y_tr)
preds = clf.predict(X_te)


# Display classification summaries
print("--- Confusion Matrix Output ---\n", confusion_matrix(y_te, preds))
print("\n--- Model Performance Report Summary ---\n", classification_report(y_te, preds))


# Proof for Question 1 (z = 0)
print(f"\n--- Concrete Trace Output ---\nWhen z = 0, Predicted Probability = {1 / (1 + np.exp(0)):.1f} (50%)")


HOMEWORK 2 — LIBRARY DEFAULTER ALERT
print("High recall: catches most actual late-returners.")
print("Low precision: many flagged students are false positives; consider")
print("the decision threshold and review false-positive cases.")

-----

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix


# Ingest dataset fields
pd.DataFrame({'Days_Overdue': [0,1,0,0,2,0,5,6,7,8,0,0], 'Defaulter': [0,0,0,0,0,0,1,1,1,1,0,0]}).to_csv('library.csv', index=False)
df = pd.read_csv('library.csv')
X_tr, X_te, y_tr, y_te = train_test_split(df[['Days_Overdue']], df['Defaulter'], test_size=0.25, random_state=42)


# Train model & predict
clf = LogisticRegression().fit(X_tr, y_tr)
preds = clf.predict(X_te)


# Display classification summaries
print("--- Confusion Matrix Output ---\n", confusion_matrix(y_te, preds))
print("\n--- Model Performance Report Summary ---\n", classification_report(y_te, preds))


''',
12: r'''
EXERCISE 12 — DECISION TREE CLASSIFICATION
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

wine = load_wine()
X, y = wine.data[:, :4], wine.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(criterion='gini', max_depth=3,
                               random_state=42).fit(X_train, y_train)
print(f"Training accuracy: {model.score(X_train, y_train) * 100:.2f}%")
print(f"Testing accuracy: {model.score(X_test, y_test) * 100:.2f}%")
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=wine.feature_names[:4],
          class_names=wine.target_names, filled=True)
plt.tight_layout()
plt.show()

-----

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load multiclass sample dataset features
wine_data = load_wine()
X_features, y_classes = wine_data.data[:, :4], wine_data.target # Filter down to 4 primary features

X_train, X_test, y_train, y_test = train_test_split(X_features, y_classes, test_size=0.2, random_state=42)

# Build a decision tree classifier with a maximum depth limit to prevent over-fitting
tree_model = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42).fit(X_train, y_train)

print(f"Training Subset Accuracy Score: {tree_model.score(X_train, y_train)*100:.2f}%")
print(f"Testing Subset Accuracy Score: {tree_model.score(X_test, y_test)*100:.2f}%")

# Generate and display a tree node splitting chart layout
plt.figure(figsize=(12, 8))
plot_tree(tree_model, feature_names=wine_data.feature_names[:4], class_names=wine_data.target_names, filled=True)
plt.show()



HOMEWORK 1 — STREAMING APP SUBSCRIPTION TRIAGE
print("The tree evaluates candidate splits and chooses the feature/threshold")
print("that gives the largest impurity reduction (or best criterion score).")

HOMEWORK 2 — MODEL OVERFITTING
# Restrict depth and/or increase min_samples_leaf to improve generalization.
regularized_tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5,
                                          random_state=42)
print("Use max_depth and min_samples_leaf; compare performance on held-out data.")
''',
13: r'''
EXERCISE 13 — SUPPORT VECTOR MACHINE (SVM)
from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = load_breast_cancer()
X, y = data.data[:, :10], data.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = SVC(kernel='linear', C=1.0).fit(X_train_scaled, y_train)
print(f"SVM test accuracy: {model.score(X_test_scaled, y_test) * 100:.2f}%")


---

from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load high-dimensional diagnostic breast cancer dataset
cancer_dataset = load_breast_cancer()
X_raw, y_labels = cancer_dataset.data[:, :10], cancer_dataset.target # Select first 10 columns

X_train, X_test, y_train, y_test = train_test_split(X_raw, y_labels, test_size=0.2, random_state=42)

# Standardize inputs because SVM relies on distance metrics
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a support vector classifier using a linear kernel boundary line
svm_engine = SVC(kernel='linear', C=1.0).fit(X_train_scaled, y_train)

print(f"SVM Test Partition Classification Accuracy: {svm_engine.score(X_test_scaled, y_test)*100:.2f}%")


HOMEWORK 1 — BIOMETRIC SIGNATURE VERIFICATION
print("Support vectors are the samples closest to the boundary. They determine")
print("the separating hyperplane and its margin between genuine and forged cases.")

HOMEWORK 2 — NON-LINEAR TUMOR CLASSIFICATION
# RBF kernel can model non-linear decision boundaries.
rbf_model = SVC(kernel='rbf', C=1.0, gamma='scale')
print("Use SVC(kernel='rbf') after scaling features; fit it on training data.")
''',
14: r'''
EXERCISE 14 — K-MEANS CLUSTERING
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
# from sklearn.datasets import make_blobs

# X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60,
#                   random_state=0)
# model = KMeans(n_clusters=4, init='k-means++', n_init=10, random_state=0)
# labels = model.fit_predict(X)
# centers = model.cluster_centers_
# plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='rainbow')
# plt.scatter(centers[:, 0], centers[:, 1], marker='X', s=250, color='black')
# plt.title('K-Means Clustering')
# plt.show()

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate an unlabelled dataset containing 4 distinct feature groups
X_unlabelled, y_true_groups = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Configure K-Means to partition data into 4 distinct clusters
kmeans_processor = KMeans(n_clusters=4, init='k-means++', n_init=10, random_state=0)
cluster_predictions = kmeans_processor.fit_predict(X_unlabelled)

# Extract final centroid coordinate positions
calculated_centroids = kmeans_processor.cluster_centers_

# Plot clustered groups with their respective centroids
plt.scatter(X_unlabelled[:, 0], X_unlabelled[:, 1], c=cluster_predictions, s=40, cmap='rainbow', label='Clustered Points')
plt.scatter(calculated_centroids[:, 0], calculated_centroids[:, 1], marker='X', s=250, color='black', label='Centroids')
plt.title('K-Means Unsupervised Clustering Assignments')
plt.legend()
plt.show()



HOMEWORK 1 — E-COMMERCE CUSTOMER PROFILING
# K-Means assigns each customer to its nearest centroid, then recalculates
# each centroid as the mean feature vector of customers assigned to it.
customers = [[120, 3], [450, 8], [80, 2], [900, 12], [300, 6], [750, 10]]
customer_model = KMeans(n_clusters=4, random_state=0, n_init=10)
customer_labels = customer_model.fit_predict(customers)
print("Customer clusters:", customer_labels)
print("Updated centroid coordinates:\n", customer_model.cluster_centers_)

HOMEWORK 2 — SATELLITE LAND-COVER MAPPING
# For a small image array, reshape RGB pixels to (N, 3), cluster them,
# then reshape labels back to image height x width.
import numpy as np
rgb_image = np.array([
    [[20, 100, 30], [25, 110, 35], [20, 40, 180]],
    [[30, 120, 40], [25, 45, 190], [150, 150, 150]]
], dtype=float)
height, width, channels = rgb_image.shape
pixels = rgb_image.reshape(-1, channels)
pixel_model = KMeans(n_clusters=3, random_state=0, n_init=10)
pixel_labels = pixel_model.fit_predict(pixels)
land_cover_map = pixel_labels.reshape(height, width)
print("Cluster labels per pixel:\n", land_cover_map)
print("RGB centroids:\n", pixel_model.cluster_centers_)
''',

15 : r'''

Exercise 1: Depth First Search (DFS)
Q1. What is the time and space complexity of DFS?
Answer: Time complexity: O(V + E), where V is the number of vertices (nodes) and E is the number of edges (connections), assuming an adjacency-list representation. DFS may visit every node and inspect every edge. Space complexity: O(V) in the worst case because the visited set and stack can store up to V nodes. In simple terms, the time depends on how many nodes and connections the graph has, while memory depends mainly on how many nodes must be tracked.
Q2. Why does DFS use a Stack?
Answer: DFS uses a stack because a stack follows LIFO: Last In, First Out. The most recently added node is explored first, so the search can continue deeper along one route before returning to earlier choices. When it reaches a dead end, it backtracks by taking another node from the stack. In the manual's code, stack.pop() removes the last item, and stack.extend(...) adds neighbouring nodes.
Exercise 2: Breadth-First Search (BFS) Shortest Path
Q1. Why is BFS guaranteed to find the shortest path while DFS is not?
Answer: BFS explores nodes level by level: first all nodes one edge away, then all nodes two edges away, and so on. Therefore, in an unweighted graph, the first time BFS reaches the goal, it has found a path with the minimum number of edges. DFS follows one route deeply and might reach the goal through a much longer route before checking a shorter one. This guarantee assumes each edge has equal cost.
Q2. What happens if the graph has weighted edges with different values?
Answer: Ordinary BFS does not guarantee the lowest-cost path when edges have different weights, because it counts edges rather than their costs. For example, a route with two edges costing 10 each may be worse than a route with three edges costing 1 each. Dijkstra's algorithm is suitable for non-negative edge weights; A* can also be used when a suitable heuristic estimate toward the goal is available.
Exercise 3: N-Queen Problem
Q1. What is backtracking search?
Answer: Backtracking is a problem-solving technique that builds a solution one choice at a time. If a choice makes the solution impossible or violates a rule, the algorithm undoes that choice and tries another. In the N-Queen problem, queens are placed row by row. If no column is safe for the current row, the algorithm returns to the previous row and moves that queen to another column.
Q2. How does the code check for diagonal conflicts in a single line?
Answer: The expression abs(r - br) == abs(c - bc) checks whether two queens are the same diagonal distance apart. Here, r and c are the row and column of the new queen, while br and bc are the row and column of an already placed queen. Two squares share a diagonal when the absolute row difference equals the absolute column difference. The code uses != to accept a placement only when this diagonal-conflict condition is false. It also checks c != bc to prevent two queens sharing a column.
Exercise 4: Tower of Hanoi
Q1. What is the recurrence relation and final time complexity of Tower of Hanoi?
Answer: The recurrence relation is T(n) = 2T(n−1) + 1. To move n disks, the algorithm first moves n−1 disks to the auxiliary rod, moves the largest disk to the destination, and then moves the n−1 disks onto it. Solving the recurrence gives 2^n − 1 moves, so the time complexity is O(2^n). For example, 3 disks require 7 moves. The number of moves grows exponentially as disks are added.
Q2. Can this problem be implemented iteratively?
Answer: Yes. Recursion is the common approach because the problem naturally breaks into smaller versions of itself, but an iterative solution is possible. It can use an explicit stack to store the steps that recursion would normally keep in function calls, or use a mathematical move pattern based on disk count and move number. The iterative version must still obey the rule that a larger disk cannot be placed on a smaller disk.
Exercise 5: Hill Climbing Optimization
Q1. What is the 'Local Maxima' trap in Hill Climbing?
Answer: A local maximum is a position whose value is better than all nearby positions, but it is not the best value across the entire search space. Hill climbing only accepts a neighbouring state if it improves the score, so it may stop at this smaller peak because reaching a better peak would require temporarily moving downhill. A global maximum, by contrast, is the best value in the whole search space.
Q2. How can you modify Hill Climbing to bypass local maxima?
Answer: One method is random restart: run hill climbing again from a different randomly selected starting point. This gives the algorithm another chance to find a better peak. Another method is simulated annealing, which sometimes permits a worse move with a controlled probability, especially early in the search. These methods reduce the chance of getting stuck, although they do not automatically guarantee the global optimum in every implementation.
Exercise 6: Missionaries and Cannibals Problem
Q1. What search strategy is used in this implementation?
Answer: The implementation uses Breadth-First Search (BFS). It stores candidate paths in a queue and removes the oldest path first, using FIFO (First In, First Out) order. It generates possible boat crossings, rejects unsafe or repeated states, and continues until it reaches the goal state. Because each crossing is treated as one step, BFS finds a solution with the fewest crossings when a solution exists.
Q2. Why must we check constraints on both the left and right banks?
Answer: The puzzle's safety rule must hold on both riverbanks. On any bank where missionaries are present, they must not be outnumbered by cannibals; otherwise, the state is invalid. If there are zero missionaries on a bank, the rule is not violated there because there is nobody to be outnumbered. Checking only the starting bank could allow an unsafe arrangement on the opposite bank, so both sides must be validated after every move.
Exercise 7: A* Algorithm
Q1. What is an 'Admissible Heuristic'?
Answer: An admissible heuristic is an estimate h(n) of the remaining cost from node n to the goal that never exceeds the true minimum remaining cost, written h(n) ≤ h*(n). A* combines the cost already paid, g(n), with the estimated remaining cost, h(n), using f(n) = g(n) + h(n). With the required conditions—particularly an admissible heuristic and appropriate graph-search handling—A* can find an optimal least-cost path. A straight-line distance that never exceeds actual travel distance is a common example.
Q2. What happens if h(n) is set to 0 everywhere?
Answer: If h(n) = 0 for every node, then f(n) = g(n) + 0 = g(n). A* therefore chooses paths based only on the cost accumulated so far, behaving like Dijkstra's algorithm in the usual non-negative-weight setting. It no longer uses an estimate to guide the search toward the goal, so it may explore more nodes, but the heuristic cannot overestimate because it is always zero.
Exercise 8: AO* Graph Search
Q1. How does an AND-OR graph differ from a standard search graph?
Answer: In a standard path-search problem, a node commonly represents alternatives: the search can choose one next route, which is an OR choice. An AND-OR graph can also represent a task that requires several sub-problems to be solved together. An OR branch needs one suitable alternative; an AND branch requires all its listed child tasks. For example, completing a project might require both designing the interface AND setting up the database, while choosing Android OR iOS is an alternative.
Q2. Why is AO* called an interactive search algorithm?
Answer: AO* repeatedly evaluates the current problem decomposition and updates estimated costs as it explores. It expands promising parts of the AND-OR graph, calculates the cost of alternatives, and propagates updated values back toward parent nodes. This top-down exploration and bottom-up cost updating work together to refine the selected solution graph. Here, 'interactive' refers to the algorithm's iterative refinement of the search and cost estimates, not necessarily interaction with a human user.
Exercise 9: Data Preprocessing & EDA
Q1. When should you use the median instead of the mean to impute missing values?
Answer: Use the median when a numerical column is strongly skewed or contains extreme outliers. The mean adds all values and divides by their count, so a very large or very small value can pull it away from a typical observation. The median is the middle value after sorting and is less affected by extreme values. For a roughly symmetric column without major outliers, the mean may be reasonable. The choice should depend on the data distribution and context.
Q2. What is the difference between data imputation and data deletion?
Answer: Imputation replaces a missing value with an estimate, such as the mean, median, or mode, so the row can remain in the dataset. Deletion removes a row or column containing missing or unsuitable data. Imputation preserves more records but can introduce bias if the replacement is inappropriate. Deletion is simpler, but it can discard useful information or leave too little data. The manual's example uses fillna() for imputation and a condition to remove implausible ages.
Exercise 10: Simple / Multiple Linear Regression
Q1. What does an R² score of 0.85 indicate?
Answer: An R² score of 0.85 means the model explains about 85% of the observed variation in the target values relative to a baseline that predicts the target mean, on the data used for evaluation. It is a measure of fit, not a statement that 85% of predictions are exactly correct. The remaining variation may come from noise, missing predictors, or limitations of the model. R² should be considered alongside other metrics and the test data results.
Q2. What is the cost function minimized by Linear Regression?
Answer: Ordinary least-squares linear regression chooses coefficients to minimize the sum of squared residuals. A residual is the difference between an actual target value and the model's predicted value. Squaring makes errors positive and penalizes larger errors more strongly. Mean Squared Error (MSE) is the average of these squared errors; minimizing RSS (sum of squared residuals) or MSE gives the same fitted coefficients when the dataset size is fixed.
Exercise 11: Logistic Regression Classifier
Q1. Why can't we use standard linear regression for categorical classification tasks?
Answer: Linear regression predicts an unrestricted numerical value, which can be below 0 or above 1. Those values are not suitable as probabilities for a binary class, and a straight-line fit is not designed to model a categorical outcome. Logistic regression instead converts a linear score into a value between 0 and 1 and uses that probability to classify an example. Linear regression can be adapted for some purposes, but it is generally not the appropriate standard model for classification.
Q2. What does the Sigmoid function do mathematically?
Answer: The sigmoid function is σ(z) = 1 / (1 + e^(−z)). It takes any real number z and maps it to a value strictly between 0 and 1. Logistic regression interprets this output as the estimated probability of the positive class. A threshold—often 0.5—can convert the probability into a class label: for example, 0.8 becomes class 1 and 0.2 becomes class 0 when the threshold is 0.5.
Exercise 12: Decision Tree Classification
Q1. What is Gini Impurity?
Answer: Gini impurity measures how mixed the class labels are inside a decision-tree node. A node containing only one class has Gini impurity 0, meaning it is pure. A node containing a mixture of classes has a higher value. The tree evaluates candidate splits and can choose one that reduces impurity, producing child nodes that contain more consistent labels. For classification, Gini impurity is commonly calculated as 1 − Σ(pᵢ²), where pᵢ is the proportion of class i in that node.
Q2. How can you prevent a decision tree from overfitting?
Answer: Overfitting happens when a tree learns details and noise in its training data so closely that it performs poorly on unseen examples. Limit its complexity by setting max_depth, increasing min_samples_split or min_samples_leaf, or pruning branches that add little predictive value. Evaluate performance on held-out test data rather than relying only on training accuracy. These controls encourage the tree to learn general patterns instead of memorizing the training set.
Exercise 13: Support Vector Machine (SVM) Classification
Q1. What are Support Vectors?
Answer: Support vectors are the training examples closest to an SVM's decision boundary. They are important because they determine the position of the separating boundary and the margin around it. Points farther away usually have less direct influence on the boundary. In simple terms, they are the critical examples that help define where one class ends and another begins.
Q2. What is the 'Kernel Trick' in SVM?
Answer: The kernel trick lets an SVM model certain nonlinear class boundaries by calculating relationships between data points as if they were represented in a higher-dimensional feature space. It avoids explicitly constructing every coordinate in that space. A linear kernel creates a linear boundary; other kernels, such as RBF, can represent more complex boundaries. The trick is useful when the classes cannot be separated well by a straight line in the original feature space.
Exercise 14: K-Means Clustering
Q1. Is K-Means sensitive to initial centroid placement?
Answer: Yes. K-Means begins with K centroids, and different initial positions can lead to different final clusters. Poor starting positions may produce a solution with higher within-cluster variation or a local optimum. The manual uses init='k-means++', which chooses initial centroids in a way that tends to spread them apart and often improves the result. Running the algorithm multiple times with n_init also helps reduce dependence on one initialization.
Q2. How do you determine the optimal number of clusters (K) for a dataset?
Answer: The Elbow Method runs K-Means for several K values and plots inertia, which measures the within-cluster sum of squared distances. Choose a K near the point where adding more clusters stops producing a large improvement—the 'elbow'. The Silhouette Score is another method; it compares how close a point is to its own cluster versus other clusters, with higher average scores generally indicating better-separated clusters. Neither method guarantees one universally correct K, so domain knowledge also matters.
Exercise 15: Case Study Reporting Matrix
Q1. Why must data preprocessing steps be documented inside a production case study deployment?
Answer: Documentation records how raw data is cleaned and converted into the format expected by the model. It should describe handling of missing values, outliers, data types, scaling, and feature selection where relevant. This makes the pipeline reproducible and helps developers apply the same transformations during training and prediction. Without consistent preprocessing, a production model may receive unexpected inputs, fail, or produce unreliable predictions. Documentation also helps with debugging, auditing, and maintenance.
Q2. How do Search Algorithms and Machine Learning models complement each other in an integrated system?
Answer: Machine Learning models learn patterns from data and make predictions or classifications—for example, identifying a package from a camera image. Search algorithms use a defined state space, possible actions, costs, and constraints to choose a route or sequence of actions—for example, using A* to guide a warehouse robot around obstacles. In an integrated system, a model can provide information about the environment while a search algorithm plans what to do with that information. They solve different but complementary parts of the overall problem.
'''
}

def main():
   
    while True:
        choice = input("\\nEnter exercise number (1-14), or Q to quit: ").strip()
        if choice.lower() in {"q", "quit", "exit"}:
            break
        try:
            number = int(choice)
        except ValueError:
            
            continue
        if number not in EXERCISES:
            
            continue
       
        print(EXERCISES[number].strip())
        

if __name__ == "__main__":
    main()
    
