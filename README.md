# GraphVisualisation

### Example Input

```
6 9
0 1 2
0 3 4
1 2 4
1 3 4
1 4 3
1 5 1
2 5 5
3 4 2
4 5 5
```

### Output 

This one is the visualisation of input graph
![Input Graph](/images/Figure_1.png)

This is the result using Kruskal's Algorithm
![Minimum Spanning Tree](/images/Figure_2.png)

### Dependencies

This project requires the following Python libraries:

- **matplotlib**: A library for creating static, animated, and interactive visualizations in Python.
- **networkx**: A library for the creation, manipulation, and study of complex networks of nodes and edges.


### Installation

To set up the project, follow these steps:

1. **Clone the Repository**

    ```bash
    git clone git@github.com:knsxw/GraphVisualisation.git
    cd GraphVisualisation
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    Install the required libraries using `pip`:

    ```bash
    pip install -r requirements.txt
    ```