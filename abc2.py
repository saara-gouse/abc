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
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60,
                  random_state=0)
model = KMeans(n_clusters=4, init='k-means++', n_init=10, random_state=0)
labels = model.fit_predict(X)
centers = model.cluster_centers_
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='rainbow')
plt.scatter(centers[:, 0], centers[:, 1], marker='X', s=250, color='black')
plt.title('K-Means Clustering')
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
'''
}

def main():
       
        print(EXERCISES)
        

if __name__ == "__main__":
    main()
